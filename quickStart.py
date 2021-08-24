#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyecharts

print(pyecharts.__version__)


# In[12]:


import pyecharts.options as opts
from pyecharts.charts import Line

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=line-stack

目前无法实现的功能:

暂无
"""


x_data = ['5000', '6000', '7000', '8000', '9000', '10000', '11000', '12000', '13000', '14000', '15000', '16000', '17000', '18000', '19000', '20000', '21000', '22000', '23000', '24000', '25000']


(
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="空锭",
        y_axis=[120, 132, 101, 134, 90, 230, 210],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add_yaxis(
        series_name="空管",
        y_axis=[220, 182, 191, 234, 290, 330, 310],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add_yaxis(
        series_name="10g纱",
        y_axis=[150, 232, 201, 154, 190, 330, 410],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add_yaxis(
        series_name="20g纱",
        y_axis=[820, 932, 901, 934, 1290, 1330, 1320],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add_yaxis(
        series_name="30g纱",
        y_axis=[320, 332, 301, 334, 390, 330, 320],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add_yaxis(
        series_name="40g纱",
        y_axis=[820, 932, 901, 934, 1290, 1330, 1320],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add_yaxis(
        series_name="50g纱",
        y_axis=[150, 232, 201, 154, 190, 330, 410],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add_yaxis(
        series_name="60g纱",
        y_axis=[320, 332, 301, 334, 390, 330, 320],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="1号锭子"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            name='功耗/w',
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(
            name='转速/min',
            type_="category", boundary_gap=False),
    )
    .render("stacked_line_chart.html")
)


# In[ ]:




