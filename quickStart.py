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


x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
y_data = [820, 932, 901, 934, 1290, 1330, 1320]


(
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="1号锭子",
        stack="总量",
        y_axis=[120, 132, 101, 134, 90, 230, 210],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="2号锭子",
        stack="总量",
        y_axis=[220, 182, 191, 234, 290, 330, 310],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="3号锭子",
        stack="总量",
        y_axis=[150, 232, 201, 154, 190, 330, 410],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="空锭的功耗"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("stacked_line_chart.html")
)


# In[ ]:




