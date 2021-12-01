import justpy as jp

def app():
    wp=jp.QuasarPage()
    h1 = jp.QDiv(a=wp,text="Analysis of Course reviews",
                 classes="text-h3 text-center q-py-xl q-px-xl")
    p1 = jp.QDiv(a=wp,text="Theese Graphs represents Courtse review analysis")
    return wp

jp.justpy(app)