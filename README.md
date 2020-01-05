## 一、项目主题
美国药物中毒基本情况和发展趋势分析  

## 二、负责部分
HTML页面及CSS样式，连接页面，编写页面内容，用python连接数据与html文档，搭建调试flask项目，部署Pythonanywhere。  


## 三、总结说明

### 1.总述     
* 图表页面  
[美国药物中毒的基本情况](http://lizhengg.pythonanywhere.com/)  
[美国药物中毒的地区情况](http://lizhengg.pythonanywhere.com/area_situation)   
[美国药物中毒的发展趋势](http://lizhengg.pythonanywhere.com/trend_situation)    
* 基本交互功能的HTML5控件丰富
 
### 2.github文档格式
文档格式正确，包含基本的templates、static、app.py/main.py、数据文档csv

### 3.技术文档书写
* HTML档描述    
1. area_situation.html和trend_situation.html是以种族来分的，Basic_situation.html是以年份来分，且分别有对应的图，通过数据绑定来实现。    
2. 均运用jinja2模板。      
3. 图的html档（共有五个）用来python档return render_template进去。       

* Python档描述    
1. 读取csv，实现每个页面均有表格且随着下拉选项筛选。  
2. 自定义函数，render_template -> 图表的显示。  
3. flask框架的路由@app.route，自定义函数 -> 页面分别为响应前和后，响应前仅有表格，响应后带图表。    
4. 仅有一个app.py文档。    

* WebApp动作描述     
1. 下拉框，运用数据绑定 -> 实现页面转换，表格随着选项转换，图表转换。   
2. 导航栏切换页面。    