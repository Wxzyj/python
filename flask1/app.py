from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline,Map,Line
from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly.graph_objects as go
import plotly as py
app = Flask(__name__)

# 准备工作
df = pd.read_csv('Mortality_States.csv')#读取
Race_available = list(df.Race.dropna().unique())#列表下拉值赋予给regions_available
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()

#第一个网页
@app.route('/',methods=['GET'])
def Basic_situation():
    Race = list(df['Race'].unique())
    Race.remove('All Races-All Origins')
    p = []
    for r in Race:
        df2 = df[df.Race == r]
        p.append(sum(df2['Deaths']))
    def pie_rich_label() -> Pie:
        c = (
            Pie()
                .add(
                "",
                [list(z) for z in zip(Race, p)],
                radius=["40%", "55%"],
                label_opts=opts.LabelOpts(
                    position="outside",
                    formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                    background_color="#eee",
                    border_color="#aaa",
                    border_width=1,
                    border_radius=4,
                    rich={
                        "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                        "abg": {
                            "backgroundColor": "#e3e3e3",
                            "width": "100%",
                            "align": "right",
                            "height": 22,
                            "borderRadius": [4, 4, 0, 0],
                        },
                        "hr": {
                            "borderColor": "#aaa",
                            "width": "100%",
                            "borderWidth": 0.5,
                            "height": 0,
                        },
                        "b": {"fontSize": 16, "lineHeight": 33},
                        "per": {
                            "color": "#eee",
                            "backgroundColor": "#334455",
                            "padding": [2, 4],
                            "borderRadius": 2,
                        },
                    },
                ),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="美国不同种族药物中毒情况"))
        )
        return c
    pie_rich_label().render()
    with open("render.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())

    def pie_rich_label2() -> Pie:
        Race1 = ['white','American Indian','asians','black','Hybrid and other_species']
        number = [72.4, 0.9,4.8,12.6,9.1]
        c = (
            Pie()
                .add(
                "",
                [list(z) for z in zip(Race1, number)],
                radius=["40%", "55%"],
                label_opts=opts.LabelOpts(
                    position="outside",
                    formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                    background_color="#eee",
                    border_color="#aaa",
                    border_width=1,
                    border_radius=4,
                    rich={
                        "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                        "abg": {
                            "backgroundColor": "#e3e3e3",
                            "width": "100%",
                            "align": "right",
                            "height": 22,
                            "borderRadius": [4, 4, 0, 0],
                        },
                        "hr": {
                            "borderColor": "#aaa",
                            "width": "100%",
                            "borderWidth": 0.5,
                            "height": 0,
                        },
                        "b": {"fontSize": 16, "lineHeight": 33},
                        "per": {
                            "color": "#eee",
                            "backgroundColor": "#334455",
                            "padding": [2, 4],
                            "borderRadius": 2,
                        },
                    },
                ),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="美国种族的分布情况"))
        )
        return c
    pie_rich_label2().render()
    with open("render.html", encoding="utf8", mode="r") as f:
        plot_all3 = "".join(f.readlines())

    data_str = df[:30].to_html()

    return render_template('Basic_situation.html',
                           the_res = data_str,
                           the_plot_all2 = plot_all2,
                           the_plot_all3=plot_all3,
                           the_select_Race=Race_available)

#第一个网页响应
@app.route('/Basic_situation_response',methods=['POST'])
def Basic_situation_response() -> 'html':
    the_region = request.form["the_Race_selected"]
    time = list(df['Year'].unique())
    Age = list(df['Age'].unique())
    Sex = list(df['Sex'].unique())
    Age.remove('All Ages')
    Sex.remove('Both Sexes')
    dfs = df.query("Race=='{}'".format(the_region))
    Race = list(df['Race'].unique())
    Race.remove('All Races-All Origins')
    p = []
    for r in Race:
        df2 = df[df.Race == r]
        p.append(sum(df2['Deaths']))
    def pie_rich_label() -> Pie:
        c = (
            Pie()
                .add(
                "",
                [list(z) for z in zip(Race, p)],
                radius=["40%", "55%"],
                label_opts=opts.LabelOpts(
                    position="outside",
                    formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                    background_color="#eee",
                    border_color="#aaa",
                    border_width=1,
                    border_radius=4,
                    rich={
                        "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                        "abg": {
                            "backgroundColor": "#e3e3e3",
                            "width": "100%",
                            "align": "right",
                            "height": 22,
                            "borderRadius": [4, 4, 0, 0],
                        },
                        "hr": {
                            "borderColor": "#aaa",
                            "width": "100%",
                            "borderWidth": 0.5,
                            "height": 0,
                        },
                        "b": {"fontSize": 16, "lineHeight": 33},
                        "per": {
                            "color": "#eee",
                            "backgroundColor": "#334455",
                            "padding": [2, 4],
                            "borderRadius": 2,
                        },
                    },
                ),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="不同种族药物中毒总体情况"))
        )
        return c
    pie_rich_label().render()
    with open("render.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())
    def pie_rich_label2() -> Pie:
        Race1 = ['white','American Indian','asians','black','Hybrid and other_species']
        number = [72.4, 0.9,4.8,12.6,9.1]
        c = (
            Pie()
                .add(
                "",
                [list(z) for z in zip(Race1, number)],
                radius=["40%", "55%"],
                label_opts=opts.LabelOpts(
                    position="outside",
                    formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                    background_color="#eee",
                    border_color="#aaa",
                    border_width=1,
                    border_radius=4,
                    rich={
                        "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                        "abg": {
                            "backgroundColor": "#e3e3e3",
                            "width": "100%",
                            "align": "right",
                            "height": 22,
                            "borderRadius": [4, 4, 0, 0],
                        },
                        "hr": {
                            "borderColor": "#aaa",
                            "width": "100%",
                            "borderWidth": 0.5,
                            "height": 0,
                        },
                        "b": {"fontSize": 16, "lineHeight": 33},
                        "per": {
                            "color": "#eee",
                            "backgroundColor": "#334455",
                            "padding": [2, 4],
                            "borderRadius": 2,
                        },
                    },
                ),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="美国种族的分布情况"))
        )
        return c
    pie_rich_label2().render()
    with open("render.html", encoding="utf8", mode="r") as f:
        plot_all3 = "".join(f.readlines())


    def timeline_bar() -> Timeline:
        x = Age
        tl = Timeline()
        for i in time:
            df2 = dfs[df.Year == int(i)]
            y1 = []
            y2 = []
            for a in Age:
                df3 = df2[df2.Age == a]
                y1.append(sum(df3['Deaths'][(df['Sex'] == 'Female')]))
                y2.append(sum(df3['Deaths'][(df['Sex'] == 'Male')]))
            bar = (
                Bar()
                    .add_xaxis(x)
                    .add_yaxis("女性死亡人数", y1)
                    .add_yaxis("男性死亡人数", y2)

                    .set_global_opts(title_opts=opts.TitleOpts("{}年{}的死亡人数".format(i,the_region)))
            )
            tl.add(bar, "{}年".format(i))
        return tl

    timeline_bar().render()
    with open("render.html", encoding="utf8", mode="r") as f:
        plot_all1 = "".join(f.readlines())

    data_str = dfs[:30].to_html()
    return render_template('Basic_situation.html',
                            the_plot_all = plot_all1,
                            the_plot_all2 =  plot_all2,
                            the_plot_all3=plot_all3,
                            the_res = data_str,
                            the_select_Race=Race_available,
                           )





#第二个页面
@app.route('/area_situation', methods=['GET'])
def area_situation():
    Year_available = list(df.Year.dropna().unique())
    cf.set_config_file(offline=True, theme="ggplot")
    py.offline.init_notebook_mode()
    data_str = df[:30].to_html()
    return render_template('area_situation.html',
                           the_res = data_str,
                           the_select_Year=Year_available)

#第二页面响应
@app.route('/area_situation_response',methods=['POST'])

def map1() -> 'html':
    Year_available = list(df.Year.dropna().unique())
    cf.set_config_file(offline=True, theme="ggplot")
    py.offline.init_notebook_mode()
    the_Year = request.form["the_Year_selected"]
    dfs = df.query("Year=='{}'".format(the_Year))
    State = list(dfs['State'].unique())
    State.remove('United States')
    p = []
    z = []
    for st in State:
        df4 = dfs[dfs.State == st]
        z.append(sum(df4['Death_Rate']))
        p.append(sum(df4['Population']))

    fig = go.Figure(data=go.Choropleth(
    locations=State,  # Spatial coordinates
    z=z,  # Data to be color-coded
    locationmode='USA-states',  # set of locations match entries in `locations`
    colorscale='Reds',
    colorbar_title="人数",
    ))

    fig.update_layout(
        title_text='1999-2017年美国各州的药物中毒人数地图可视化',
        geo_scope='usa',  # limite map scope to USA
    )

    py.offline.plot(fig, filename="us.html", auto_open=False)
    with open("us.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())

    fig = go.Figure(data=go.Choropleth(
    locations=State,  # Spatial coordinates
    z=p,  # Data to be color-coded
    locationmode='USA-states',  # set of locations match entries in `locations`
    colorscale='Reds',
    colorbar_title="人数",
    ))

    fig.update_layout(
        title_text='1999-2017年美国各州的人数地图可视化',
        geo_scope='usa',  # limite map scope to USA
    )

    py.offline.plot(fig, filename="us.html", auto_open=False)
    with open("us.html", encoding="utf8", mode="r") as f:
        plot_all3 = "".join(f.readlines())

    data_str = dfs[:30].to_html()
    return render_template('area_situation.html',
                           the_plot_all2 = plot_all2,
                           the_plot_all3 = plot_all3,
                            the_res = data_str,
                            the_select_Year=Year_available,
                           )



#第三页面
@app.route('/trend_situation',methods=['GET'])
def trend_situation():
    Race_available = list(df.Race.dropna().unique())  # 列表下拉值赋予给regions_available
    cf.set_config_file(offline=True, theme="ggplot")
    py.offline.init_notebook_mode()
    data_str = df[:30].to_html()
    def line_markline2() -> Line:
        df = pd.read_csv('Mortality_States.csv')
        time = list(df['Year'].unique())
        times = []
        for t in list(time):
            times.append(str(t))

        Race1 = list(df['Race'].unique())
        r2 = []
        for r in Race1:
            df5 = df[df.Race == r]
            r1 = []
            r2.append(r1)
            for t in time:
                df6 = df5[df5.Year == t]
                r1.append(int(sum(df6['Death_Rate'])))
        c = (
            Line()
                .add_xaxis(times)
                .add_yaxis(
                "All Races-All Origins",
                r2[0],
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
            )
                .add_yaxis(
                "Hispanic",
                r2[1],
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
            )
                .add_yaxis(
                "Non-Hispanic Black",
                r2[2],
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
            )
                .add_yaxis(
                "Non-Hispanic White",
                r2[3],
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="种族药物中毒死亡率"))
        )
        return c
    line_markline2().render()
    with open("render.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())
    return render_template('trend_situation.html',
                           the_plot_all2=plot_all2,
                           the_res = data_str,
                           the_select_Race=Race_available)

@app.route('/trend_situation_response',methods=['POST'])
def trend_situation_response() -> 'html':
    Race_available = list(df.Race.dropna().unique())  # 列表下拉值赋予给regions_available
    cf.set_config_file(offline=True, theme="ggplot")
    py.offline.init_notebook_mode()
    the_Race = request.form["the_Race_selected"]
    time = list(df['Year'].unique())
    Age = list(df['Age'].unique())
    Sex = list(df['Sex'].unique())
    Age.remove('All Ages')
    Sex.remove('Both Sexes')
    dfs = df.query("Race=='{}'".format(the_Race))

    def line_markline() -> Line:
        the_region = request.form["the_Race_selected"]
        yy1 = []
        yy2 = []
        times = []
        for t in list(time):
            times.append(str(t))
        for t in time:
            df5 = dfs[dfs.Year == t]
            yy1.append(sum(df5['Deaths'][(df['Sex'] == 'Female')]))
            yy2.append(sum(df5['Deaths'][(df['Sex'] == 'Male')]))
        c = (
            Line()
                .add_xaxis(times)
                .add_yaxis(
                "女性",
                yy1,
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
            )
                .add_yaxis(
                "男性",
                yy2,
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="1999-2017年{}的死亡人数".format(the_region)))
        )
        return c

    line_markline().render()
    with open("render.html", encoding="utf8", mode="r") as f:
        plot_all3 = "".join(f.readlines())


    def line_markline2() -> Line:
        df = pd.read_csv('Mortality_States.csv')
        time = list(df['Year'].unique())
        times = []
        for t in list(time):
            times.append(str(t))

        Race1 = list(df['Race'].unique())
        r2 = []
        for r in Race1:
            df5 = df[df.Race == r]
            r1 = []
            r2.append(r1)
            for t in time:
                df6 = df5[df5.Year == t]
                r1.append(int(sum(df6['Death_Rate'])))
        c = (
            Line()
                .add_xaxis(times)
                .add_yaxis(
                "All Races-All Origins",
                r2[0],
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
            )
                .add_yaxis(
                "Hispanic",
                r2[1],
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
            )
                .add_yaxis(
                "Non-Hispanic Black",
                r2[2],
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
            )
                .add_yaxis(
                "Non-Hispanic White",
                r2[3],
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="种族药物中毒死亡率"))
        )
        return c

    line_markline2().render()
    with open("render.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())

    data_str = dfs[:30].to_html()
    return render_template('trend_situation.html',
                            the_plot_all2=plot_all2,
                            the_plot_all3 = plot_all3,
                            the_res = data_str,
                            the_select_Race=Race_available,
                           )


if __name__ == '__main__':
    app.run(debug=True,port=8000)
