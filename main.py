from flask import Flask, render_template, request
from langchain.text_splitter import CharacterTextSplitter, Language,RecursiveCharacterTextSplitter, TokenTextSplitter
import os
app = Flask(__name__)


def chunk_with_spans(text, splitter):
    chunks = splitter.split_text(text)
    spans = []
    start = 0
    for chunk in chunks:
        idx = text.find(chunk, start)
        spans.append((idx, idx + len(chunk)))  # (start, end)
        start = idx + 1
    return spans, chunks



def highlight_text(text, spans, colors):
    cut_points = {0, len(text)}
    for i, (start, end) in enumerate(spans):
        cut_points.add(start)
        cut_points.add(end)
    cut_points = sorted(cut_points)

    html_parts = []
    for i in range(len(cut_points) - 1):
        seg_start, seg_end = cut_points[i], cut_points[i+1]
        segment = text[seg_start:seg_end]

        # Find active chunks covering this segment
        active_colors = []
        for j, (s, e) in enumerate(spans):
            if s < seg_end and e > seg_start:
                active_colors.append(colors[j % len(colors)])

        if active_colors:
            if len(active_colors) == 1:
                color = active_colors[0]
            else:
                color = "#90a955"
            html_parts.append(f"<span style='background-color:{color}'>{segment}</span>")
        else:
            html_parts.append(segment)

    return "".join(html_parts)




@app.route('/', methods=["GET","POST"])
def home():
    result_html = None
    text = """Artificial intelligence (AI) is the capability of computational systems to perform tasks typically associated with human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making. It is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and use learning and intelligence to take actions that maximize their chances of achieving defined goals. High-profile applications of AI include advanced web search engines (e.g., Google Search); recommendation systems (used by YouTube, Amazon, and Netflix); virtual assistants (e.g., Google Assistant, Siri, and Alexa); autonomous vehicles (e.g., Waymo); generative and creative tools (e.g., language models and AI art); and superhuman play and analysis in strategy games (e.g., chess and Go). However, many AI applications are not perceived as AI: "A lot of cutting edge AI has filtered into general applications, often without being called AI because once something becomes useful enough and common enough it's not labeled AI anymore." """
    chunk_size = 20
    chunk_overlap = 5
    splitter_type = 'char'
    splitter = CharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap,separator="")
    if request.method == "POST":
        text = request.form['text']
        splitter_type = request.form['splitter']
        chunk_size = int(request.form['chunk_size'])
        chunk_overlap = int(request.form['chunk_overlap'])
        if(splitter_type=='char'):
            splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap,separator='')
        elif splitter_type == 'recursive-python':
            splitter = RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON,chunk_size=chunk_size,chunk_overlap=chunk_overlap)
        elif splitter_type == 'recursive-js':
            splitter = RecursiveCharacterTextSplitter.from_language(language=Language.JS,chunk_size=chunk_size,chunk_overlap=chunk_overlap)
        elif splitter_type == 'recursive-markdown' :
            splitter = RecursiveCharacterTextSplitter.from_language(language=Language.MARKDOWN,chunk_size=chunk_size,chunk_overlap=chunk_overlap)
        spans, chunks = chunk_with_spans(text, splitter)
        print(chunks)
        colors = [
    "#70d6ff",  # red
    "#e9ff70",  # green
    "#ff9770",  # blue
    "#ff70a6"   # yellow
]
        result_html = highlight_text(text, spans, colors)
        
    return render_template('home.html', result=result_html,text =text,chunk_size=chunk_size,chunk_overlap=chunk_overlap)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

