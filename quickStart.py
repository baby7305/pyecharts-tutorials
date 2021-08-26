#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyecharts

print(pyecharts.__version__)


# In[3]:


import pandas as pd
df = pd.read_csv('电锭带载功耗 - 复核0820.csv')
print(df)


# In[5]:


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
        series_name="1号锭子",
        y_axis=df.loc[0].values,
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add_yaxis(
        series_name="2号锭子",
        y_axis=df['25000'].values,
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add_yaxis(
        series_name="3号锭子",
        y_axis=[150, 232, 201, 154, 190, 330, 410],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="空锭的功耗"),
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




