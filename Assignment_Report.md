# 作业一：数据探索性分析与数据预处理
## 汇报人
- 汪汗青 2120171064
## 环境
- python3.5
- numpy
- matplotlib
- sklearn
- [MICE](https://github.com/qweas120/MICE)

----------------------------------

## 数据说明
### 本报告使用的数据源有2个：
1. NFL Play-by-Play 2009-2017数据集，共计102项属性，407688个数据条目。
2. San Francisco Building Permits数据集，共计43项属性，198900个数据条目。

## 数据可视化和摘要

### **数据摘要**
- 对标称属性的处理
    - 对于数据集1，共筛选出标称属性56个，属性ID详见`Data/nominal_0`，。
    - 对于数据集2，共筛选出标称属性36个，属性ID详见`Data/nominal_1`。 <br> 对于每一个标称属性，统计其所有值的频数，频数统计结果见`frequency_0.txt`和`frequency_1.txt`。实现如下
    ```python
        # database_id is the index of the database
        with open('Data/nominal_%d'%database_id,'r') as fp:
                nominal = [int(n)-1 for n in fp.read().split(' ')]

        with open(database[database_id],encoding='utf-8') as fp:
            reader =  csv.reader(fp)
            for row in reader:
                event.append(row)

        num_att = len(event[0])
        cnt = len(event)
        
        with open('frequency_%d.txt'%database_id,'w',encoding='utf-8') as fp:
            for n in nominal:
                dic = {}
                attr = event[0][n]
                for i in range(1, cnt):
                    x =  len(event[i])
                    val = event[i][n]
                    if val in dic:
                        dic[val] += 1
                    else:
                        dic[val] = 1
                fp.write('Attribute %s\n'%attr)
                for val in dic:
                    fp.write('%s %d\n'%(val,dic[val]))
    ```
    
- 对数值属性的处理<br>数据集中的数值属性最大、最小、均值、中位数、四分位数及缺失值的个数如下表所示

**<center>NFL Play by Play 2009-2017</center>**

| attr_name | Max | Min | Mean | Median | Q1 | Q3 | NA |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Drive|35.00|1.00|12.32|12.00|6.00|18.00|0|
|qtr|5.00|1.00|2.58|3.00|2.00|4.00|0|
|down|4.00|1.00|2.00|2.00|1.00|3.00|61154|
|TimeUnder|15.00|0.00|7.37|7.00|3.00|11.00|0|
|TimeSecs|3600.00|-900.00|1695.27|1800.00|778.00|2585.00|224|
|PlayTimeDiff|943.00|0.00|20.58|17.00|5.00|37.00|444|
|yrdln|50.00|1.00|28.49|30.00|20.00|39.00|840|
|yrdline100|99.00|1.00|48.64|49.00|30.00|70.00|840|
|ydstogo|50.00|0.00|7.31|9.00|3.00|10.00|0|
|ydsnet|99.00|-87.00|25.95|19.00|5.00|43.00|0|
|Yards.Gained|99.00|-74.00|4.99|1.00|0.00|7.00|0|
|Safety|1.00|0.00|0.00|0.00|0.00|0.00|0|
|Onsidekick|1.00|0.00|0.00|0.00|0.00|0.00|0|
|AirYards|84.00|-70.00|3.26|0.00|0.00|4.00|0|
|YardsAfterCatch|90.00|-81.00|1.25|0.00|0.00|0.00|0|
|FieldGoalDistance|71.00|18.00|37.47|38.00|29.00|46.00|398740|
|PosTeamScore|61.00|0.00|10.20|7.00|2.00|16.00|26904|
|DefTeamScore|61.00|0.00|11.41|10.00|3.00|17.00|26904|
|ScoreDiff|59.00|-59.00|-1.19|0.00|-7.00|4.00|24988|
|AbsScoreDiff|59.00|0.00|7.78|7.00|3.00|11.00|26904|
|posteam_timeouts_pre|3.00|0.00|2.52|3.00|2.00|3.00|0|
|HomeTimeouts_Remaining_Pre|3.00|-3.00|2.54|3.00|2.00|3.00|0|
|AwayTimeouts_Remaining_Pre|3.00|-1.00|2.52|3.00|2.00|3.00|0|
|HomeTimeouts_Remaining_Post|3.00|-3.00|2.52|3.00|2.00|3.00|0|
|AwayTimeouts_Remaining_Post|3.00|-1.00|2.50|3.00|2.00|3.00|0|
|No_Score_Prob|1.00|0.00|0.13|0.02|0.00|0.17|176|
|Opp_Field_Goal_Prob|0.36|0.00|0.09|0.08|0.03|0.15|176|
|Opp_Safety_Prob|0.03|0.00|0.00|0.00|0.00|0.00|176|
|Opp_Touchdown_Prob|0.50|0.00|0.14|0.12|0.04|0.23|176|
|Field_Goal_Prob|0.99|0.00|0.24|0.23|0.15|0.33|176|
|Safety_Prob|0.02|0.00|0.00|0.00|0.00|0.00|176|
|Touchdown_Prob|0.91|0.00|0.30|0.31|0.19|0.41|176|
|ExPoint_Prob|0.99|0.00|0.02|0.00|0.00|0.00|0|
|TwoPoint_Prob|0.47|0.00|0.00|0.00|0.00|0.00|0|
|ExpPts|6.50|-3.84|1.57|1.26|0.32|2.88|176|
|EPA|9.51|-13.49|0.02|0.00|-0.60|0.56|369|
|airEPA|7.35|-12.85|0.52|0.30|-0.50|1.39|248394|
|yacEPA|9.56|-14.00|-0.39|0.00|-0.96|0.49|248498|
|Home_WP_pre|1.00|0.00|0.53|0.53|0.33|0.77|24954|
|Away_WP_pre|1.00|0.00|0.47|0.47|0.23|0.68|24954|
|Home_WP_post|1.00|0.00|0.53|0.53|0.32|0.77|26587|
|Away_WP_post|1.00|0.00|0.47|0.47|0.23|0.68|26587|
|Win_Prob|1.00|0.00|0.50|0.50|0.28|0.73|25009|
|WPA|0.99|-1.00|0.00|0.00|-0.01|0.01|5541|
|airWPA|0.99|-1.00|0.02|0.00|-0.01|0.04|248501|
|yacWPA|1.00|-0.99|-0.01|0.00|-0.02|0.01|248762|


<br><br>

**<center>San Francisco Building Permits</center>**

| attr_name | Max | Min | Mean | Median | Q1 | Q3 | NA |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Unit|6004.00|0.00|78.52|0.00|0.00|1.00|169421|
|Number of Existing Stories|78.00|0.00|5.71|3.00|2.00|4.00|42784|
|Number of Proposed Stories|78.00|0.00|5.75|3.00|2.00|4.00|42868|
|Estimated Cost|537958646.00|1.00|168955.44|11000.00|3300.00|35000.00|38066|
|Revised Cost|780500000.00|0.00|132856.19|7000.00|1.00|28710.00|6066|
|Proposed Units|1911.00|0.00|16.51|2.00|1.00|4.00|50911|
|Plansets|9000.00|0.00|1.27|2.00|0.00|2.00|37309|

实现如下
```python
    for i in range(0, num_att):
            if i in nominal:
                continue
            name = event[0][i]
            count = 0
            lost = 0
            ar = []
            for j in range(1,cnt):
                val = event[j][i]
                if val in NA:
                    lost += 1
                else:
                    ar.append(float(val))
                    count += 1
            
            ar = np.array(sorted(ar))
            maxx = ar.max()
            minn = ar.min()
            mean = ar.mean()
            medi = ar[int(count/2)]
            q1 = ar[int(count/4)]
            q3 = ar[int(count/4*3)]
```


### **数据可视化**

为了对数据的各项属性分布进行分析，实践分别对两个数据集的各项属性绘制了直方图（bins=20）、Q-Q图和盒图。分别用于可视化数据的具体分布、验证是否为正态分布以及观察离群点。对于Q-Q图，横坐标为标准正态分布的百分位数，纵坐标为对应属性的百分位数，若散点的分布靠近一条直线，则说明数据分布接近正态分布，该直线的斜率为正态分布的标准差，截距为均值。<br>
以下为可视化结果。

#### NFL Play by Play 2009-2017 属性可视化


**Drive**

<table>
<tr>
<th><img src="Figures/Drive_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Drive_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Drive_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**qtr**

<table>
<tr>
<th><img src="Figures/qtr_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_qtr_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_qtr_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**down**

<table>
<tr>
<th><img src="Figures/down_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_down_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_down_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**TimeUnder**

<table>
<tr>
<th><img src="Figures/TimeUnder_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_TimeUnder_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_TimeUnder_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**TimeSecs**

<table>
<tr>
<th><img src="Figures/TimeSecs_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_TimeSecs_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_TimeSecs_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**PlayTimeDiff**

<table>
<tr>
<th><img src="Figures/PlayTimeDiff_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_PlayTimeDiff_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_PlayTimeDiff_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**yrdln**

<table>
<tr>
<th><img src="Figures/yrdln_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_yrdln_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_yrdln_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**yrdline100**

<table>
<tr>
<th><img src="Figures/yrdline100_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_yrdline100_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_yrdline100_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**ydstogo**

<table>
<tr>
<th><img src="Figures/ydstogo_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_ydstogo_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_ydstogo_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**ydsnet**

<table>
<tr>
<th><img src="Figures/ydsnet_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_ydsnet_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_ydsnet_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Yards.Gained**

<table>
<tr>
<th><img src="Figures/Yards.Gained_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Yards.Gained_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Yards.Gained_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Safety**

<table>
<tr>
<th><img src="Figures/Safety_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Safety_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Safety_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**AirYards**

<table>
<tr>
<th><img src="Figures/AirYards_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_AirYards_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_AirYards_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**YardsAfterCatch**

<table>
<tr>
<th><img src="Figures/YardsAfterCatch_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_YardsAfterCatch_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_YardsAfterCatch_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**FieldGoalDistance**

<table>
<tr>
<th><img src="Figures/FieldGoalDistance_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_FieldGoalDistance_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_FieldGoalDistance_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**PosTeamScore**

<table>
<tr>
<th><img src="Figures/PosTeamScore_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_PosTeamScore_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_PosTeamScore_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**DefTeamScore**

<table>
<tr>
<th><img src="Figures/DefTeamScore_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_DefTeamScore_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_DefTeamScore_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**ScoreDiff**

<table>
<tr>
<th><img src="Figures/ScoreDiff_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_ScoreDiff_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_ScoreDiff_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**AbsScoreDiff**

<table>
<tr>
<th><img src="Figures/AbsScoreDiff_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_AbsScoreDiff_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_AbsScoreDiff_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**posteam_timeouts_pre**

<table>
<tr>
<th><img src="Figures/posteam_timeouts_pre_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_posteam_timeouts_pre_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_posteam_timeouts_pre_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**HomeTimeouts_Remaining_Pre**

<table>
<tr>
<th><img src="Figures/HomeTimeouts_Remaining_Pre_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_HomeTimeouts_Remaining_Pre_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_HomeTimeouts_Remaining_Pre_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**AwayTimeouts_Remaining_Pre**

<table>
<tr>
<th><img src="Figures/AwayTimeouts_Remaining_Pre_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_AwayTimeouts_Remaining_Pre_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_AwayTimeouts_Remaining_Pre_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**HomeTimeouts_Remaining_Post**

<table>
<tr>
<th><img src="Figures/HomeTimeouts_Remaining_Post_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_HomeTimeouts_Remaining_Post_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_HomeTimeouts_Remaining_Post_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**AwayTimeouts_Remaining_Post**

<table>
<tr>
<th><img src="Figures/AwayTimeouts_Remaining_Post_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_AwayTimeouts_Remaining_Post_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_AwayTimeouts_Remaining_Post_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**No_Score_Prob**

<table>
<tr>
<th><img src="Figures/No_Score_Prob_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_No_Score_Prob_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_No_Score_Prob_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Opp_Field_Goal_Prob**

<table>
<tr>
<th><img src="Figures/Opp_Field_Goal_Prob_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Opp_Field_Goal_Prob_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Opp_Field_Goal_Prob_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Opp_Safety_Prob**

<table>
<tr>
<th><img src="Figures/Opp_Safety_Prob_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Opp_Safety_Prob_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Opp_Safety_Prob_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Opp_Touchdown_Prob**

<table>
<tr>
<th><img src="Figures/Opp_Touchdown_Prob_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Opp_Touchdown_Prob_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Opp_Touchdown_Prob_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Field_Goal_Prob**

<table>
<tr>
<th><img src="Figures/Field_Goal_Prob_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Field_Goal_Prob_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Field_Goal_Prob_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Safety_Prob**

<table>
<tr>
<th><img src="Figures/Safety_Prob_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Safety_Prob_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Safety_Prob_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Touchdown_Prob**

<table>
<tr>
<th><img src="Figures/Touchdown_Prob_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Touchdown_Prob_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Touchdown_Prob_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**ExPoint_Prob**

<table>
<tr>
<th><img src="Figures/ExPoint_Prob_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_ExPoint_Prob_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_ExPoint_Prob_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**TwoPoint_Prob**

<table>
<tr>
<th><img src="Figures/TwoPoint_Prob_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_TwoPoint_Prob_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_TwoPoint_Prob_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**ExpPts**

<table>
<tr>
<th><img src="Figures/ExpPts_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_ExpPts_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_ExpPts_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**EPA**

<table>
<tr>
<th><img src="Figures/EPA_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_EPA_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_EPA_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**airEPA**

<table>
<tr>
<th><img src="Figures/airEPA_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_airEPA_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_airEPA_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**yacEPA**

<table>
<tr>
<th><img src="Figures/yacEPA_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_yacEPA_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_yacEPA_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Home_WP_pre**

<table>
<tr>
<th><img src="Figures/Home_WP_pre_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Home_WP_pre_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Home_WP_pre_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Away_WP_pre**

<table>
<tr>
<th><img src="Figures/Away_WP_pre_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Away_WP_pre_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Away_WP_pre_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Home_WP_post**

<table>
<tr>
<th><img src="Figures/Home_WP_post_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Home_WP_post_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Home_WP_post_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Away_WP_post**

<table>
<tr>
<th><img src="Figures/Away_WP_post_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Away_WP_post_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Away_WP_post_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Win_Prob**

<table>
<tr>
<th><img src="Figures/Win_Prob_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Win_Prob_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Win_Prob_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**WPA**

<table>
<tr>
<th><img src="Figures/WPA_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_WPA_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_WPA_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**airWPA**

<table>
<tr>
<th><img src="Figures/airWPA_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_airWPA_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_airWPA_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**yacWPA**

<table>
<tr>
<th><img src="Figures/yacWPA_0.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_yacWPA_0.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_yacWPA_0.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


#### San Francisco Building Permits 属性可视化


**Unit**

<table>
<tr>
<th><img src="Figures/Unit_1.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Unit_1.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Unit_1.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Number of Existing Stories**

<table>
<tr>
<th><img src="Figures/Number of Existing Stories_1.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Number of Existing Stories_1.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Number of Existing Stories_1.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Number of Proposed Stories**

<table>
<tr>
<th><img src="Figures/Number of Proposed Stories_1.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Number of Proposed Stories_1.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Number of Proposed Stories_1.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Estimated Cost**

<table>
<tr>
<th><img src="Figures/Estimated Cost_1.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Estimated Cost_1.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Estimated Cost_1.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Revised Cost**

<table>
<tr>
<th><img src="Figures/Revised Cost_1.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Revised Cost_1.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Revised Cost_1.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Proposed Units**

<table>
<tr>
<th><img src="Figures/Proposed Units_1.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Proposed Units_1.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Proposed Units_1.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>


**Plansets**

<table>
<tr>
<th><img src="Figures/Plansets_1.png" width="250px"><p>Histogram</p></th>
<th><img src="Figures/qq_Plansets_1.png" width="250px"><p>Q-Q plot</p></th>
<th><img src="Figures/box_Plansets_1.png" width="250px"><p>Boxplot</p></th>
</tr>
</table>


--------------------
<br>



实现如下
```python

    for i in range(0, num_att):
        if i in nominal:
            continue
        name = event[0][i]

        # print(i, name)
        count = 0
        lost = 0
        ar = []
        for j in range(1,cnt):
            val = event[j][i]
            if val in NA:
                lost += 1
            else:
                ar.append(float(val))
                count += 1
        
        ar = np.array(sorted(ar))
        
        plt.hist(ar,20)
        plt.savefig('Figures/%s_%d.png'%(name,database_id))
        plt.close()
        y = []
        for j in range(100):
            y.append(ar[int(count*(1.0*(j)/100))])
        y = np.array(y)
        plt.scatter(x,y)
        plt.savefig('Figures/qq_%s_%d.png'%(name,database_id))
        plt.close()
        plt.boxplot([ar],labels=[name])
        plt.savefig('Figures/box_%s_%d.png'%(name,database_id))
        plt.close()

```

## 数据缺失的处理
经对数据的观察发现，两个数据集中出现的缺失主要有两种，一种是由于项目本身的逻辑造成的缺失，某些属性是否存在依赖于前一个属性的布尔值的真假来决定的，若为假，从逻辑上应该没有这些属性。
另一种缺失是在录入条目时未填写而产生的缺失。对数据缺失的处理主要针对第二种缺失，并采用下列四种方式进行处理：
1. 将缺失部分剔除
2. 用最高频率值来填补缺失值
3. 通过属性的相关关系来填补缺失值
4. 通过数据对象之间的相似性来填补缺失值

从实验结果来看，不同的处理方式对分布会产生不同的变化，效果的优劣与特定属性相关。填补后的数据分布如下所示:<br>
#### NFL Play by Play 2009-2017 缺失值填补对比



**down**

<table>
<tr>
<th><img src="Figures/down_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_down_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_down_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_down_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**TimeSecs**

<table>
<tr>
<th><img src="Figures/TimeSecs_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_TimeSecs_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_TimeSecs_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_TimeSecs_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**PlayTimeDiff**

<table>
<tr>
<th><img src="Figures/PlayTimeDiff_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_PlayTimeDiff_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_PlayTimeDiff_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_PlayTimeDiff_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**yrdln**

<table>
<tr>
<th><img src="Figures/yrdln_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_yrdln_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_yrdln_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_yrdln_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**yrdline100**

<table>
<tr>
<th><img src="Figures/yrdline100_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_yrdline100_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_yrdline100_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_yrdline100_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**PosTeamScore**

<table>
<tr>
<th><img src="Figures/PosTeamScore_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_PosTeamScore_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_PosTeamScore_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_PosTeamScore_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**DefTeamScore**

<table>
<tr>
<th><img src="Figures/DefTeamScore_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_DefTeamScore_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_DefTeamScore_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_DefTeamScore_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**ScoreDiff**

<table>
<tr>
<th><img src="Figures/ScoreDiff_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_ScoreDiff_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_ScoreDiff_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_ScoreDiff_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**AbsScoreDiff**

<table>
<tr>
<th><img src="Figures/AbsScoreDiff_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_AbsScoreDiff_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_AbsScoreDiff_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_AbsScoreDiff_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**No_Score_Prob**

<table>
<tr>
<th><img src="Figures/No_Score_Prob_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_No_Score_Prob_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_No_Score_Prob_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_No_Score_Prob_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Opp_Field_Goal_Prob**

<table>
<tr>
<th><img src="Figures/Opp_Field_Goal_Prob_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Opp_Field_Goal_Prob_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Opp_Field_Goal_Prob_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Opp_Field_Goal_Prob_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Opp_Safety_Prob**

<table>
<tr>
<th><img src="Figures/Opp_Safety_Prob_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Opp_Safety_Prob_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Opp_Safety_Prob_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Opp_Safety_Prob_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Opp_Touchdown_Prob**

<table>
<tr>
<th><img src="Figures/Opp_Touchdown_Prob_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Opp_Touchdown_Prob_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Opp_Touchdown_Prob_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Opp_Touchdown_Prob_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Field_Goal_Prob**

<table>
<tr>
<th><img src="Figures/Field_Goal_Prob_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Field_Goal_Prob_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Field_Goal_Prob_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Field_Goal_Prob_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Safety_Prob**

<table>
<tr>
<th><img src="Figures/Safety_Prob_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Safety_Prob_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Safety_Prob_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Safety_Prob_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Touchdown_Prob**

<table>
<tr>
<th><img src="Figures/Touchdown_Prob_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Touchdown_Prob_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Touchdown_Prob_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Touchdown_Prob_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**ExpPts**

<table>
<tr>
<th><img src="Figures/ExpPts_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_ExpPts_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_ExpPts_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_ExpPts_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**EPA**

<table>
<tr>
<th><img src="Figures/EPA_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_EPA_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_EPA_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_EPA_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**airEPA**

<table>
<tr>
<th><img src="Figures/airEPA_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_airEPA_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_airEPA_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_airEPA_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**yacEPA**

<table>
<tr>
<th><img src="Figures/yacEPA_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_yacEPA_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_yacEPA_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_yacEPA_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Home_WP_pre**

<table>
<tr>
<th><img src="Figures/Home_WP_pre_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Home_WP_pre_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Home_WP_pre_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Home_WP_pre_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Away_WP_pre**

<table>
<tr>
<th><img src="Figures/Away_WP_pre_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Away_WP_pre_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Away_WP_pre_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Away_WP_pre_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Home_WP_post**

<table>
<tr>
<th><img src="Figures/Home_WP_post_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Home_WP_post_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Home_WP_post_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Home_WP_post_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Away_WP_post**

<table>
<tr>
<th><img src="Figures/Away_WP_post_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Away_WP_post_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Away_WP_post_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Away_WP_post_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Win_Prob**

<table>
<tr>
<th><img src="Figures/Win_Prob_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Win_Prob_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Win_Prob_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Win_Prob_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**WPA**

<table>
<tr>
<th><img src="Figures/WPA_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_WPA_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_WPA_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_WPA_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**airWPA**

<table>
<tr>
<th><img src="Figures/airWPA_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_airWPA_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_airWPA_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_airWPA_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**yacWPA**

<table>
<tr>
<th><img src="Figures/yacWPA_0.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_yacWPA_0.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_yacWPA_0.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_yacWPA_0.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


#### San Francisco Building Permits 缺失值填补对比



**Unit**

<table>
<tr>
<th><img src="Figures/Unit_1.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Unit_1.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Unit_1.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Unit_1.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Number of Existing Stories**

<table>
<tr>
<th><img src="Figures/Number of Existing Stories_1.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Number of Existing Stories_1.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Number of Existing Stories_1.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Number of Existing Stories_1.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Number of Proposed Stories**

<table>
<tr>
<th><img src="Figures/Number of Proposed Stories_1.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Number of Proposed Stories_1.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Number of Proposed Stories_1.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Number of Proposed Stories_1.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Estimated Cost**

<table>
<tr>
<th><img src="Figures/Estimated Cost_1.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Estimated Cost_1.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Estimated Cost_1.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Estimated Cost_1.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Revised Cost**

<table>
<tr>
<th><img src="Figures/Revised Cost_1.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Revised Cost_1.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Revised Cost_1.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Revised Cost_1.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Proposed Units**

<table>
<tr>
<th><img src="Figures/Proposed Units_1.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Proposed Units_1.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Proposed Units_1.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Proposed Units_1.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>


**Plansets**

<table>
<tr>
<th><img src="Figures/Plansets_1.png" width="200px"><p>剔除缺失</p></th>
<th><img src="Figures/mf_Plansets_1.png" width="200px"><p>高频填补</p></th>
<th><img src="Figures/cm_Plansets_1.png" width="200px"><p>相关属性填补</p></th>
<th><img src="Figures/knn_Plansets_1.png" width="200px"><p>KNN填补</p></th>
</tr>
</table>


--------------------
<br>



核心实现如下
```python

def impute(database_id):
    from sklearn.linear_model import LinearRegression
    from utils.skmice import MiceImputer
    from sklearn.neighbors import NearestNeighbors
    cnt = 0
    with open('Data/NA_%d'%database_id,'r') as fp:
        nas = [int(n)-1 for n in fp.read().split(' ')]

    with open(database[database_id],encoding='utf-8') as fp:
    # with open(database[database_id]) as fp:
        reader =  csv.reader(fp)
        for row in reader:
            event.append(row)
            cnt += 1

    num_att = len(event[0])

    # Impute with the most frequence value
    for i in nas:
        name = event[0][i]
        dic = {}
        maxx = 0
        max_val = 0
        lost = 0
        ar = []
        for j in range(1,cnt):
            val = event[j][i]
            if val not in NA:
                val = float(val)
                ar.append(val)
                if val in dic:
                    dic[val] += 1
                else:
                    dic[val] = 1
                if maxx < dic[val]:
                    maxx = dic[val]
                    max_val = val
            else:
                lost += 1
        
        for j in range(lost):
            ar.append(max_val)
        
        ar = np.array(ar)
        plt.hist(ar,20)
        plt.savefig('Figures/mf_%s_%d.png'%(name,database_id))
        plt.close()
    

    # Impute with the corelation matrix
    ar = []
    for i in nas:
        name = event[0][i]
        temp = []

        for j in range(1,cnt):
            val = event[j][i]
            if val not in NA:
                val = float(val)
                temp.append(val)
            else:
                temp.append(np.nan)

        ar.append(temp)
    
    ar = np.array(ar)
    ar = np.transpose(ar)
    # print(ar.shape)

    # ar = ar[:101,:]
    # cnt = ar.shape[0]
    batch_num = 1000
    imputer = MiceImputer()
    batchsize = int((cnt)/batch_num)
    for i in range(batch_num):
        print(i)
        if i == batch_num - 1:
            ar[i*batchsize:,:] = imputer.transform(ar[i*batchsize:,:], LinearRegression, 5)
        else:
            ar[i*batchsize:(i+1)*batchsize,:] = imputer.transform(ar[i*batchsize:(i+1)*batchsize,:], LinearRegression, 5)
    # print(ar.shape)
    for _,i in enumerate(nas):
        # print(name)
        # print(ar[:,_])
        name = event[0][i]
        plt.hist(ar[:,_],20)
        plt.savefig('Figures/cm_%s_%d.png'%(name,database_id))
        plt.close()
    
    # Impute using KNN
    ar = []
    for i in nas:
        name = event[0][i]
        temp = []

        for j in range(1,cnt):
            val = event[j][i]
            if val not in NA:
                val = float(val)
                temp.append(val)
            else:
                temp.append(np.nan)

        ar.append(temp)
    
    ar = np.array(ar)
    ar = np.transpose(ar)

    batchsize = int((cnt)/1000)
    for i in range(1000):
        if i == 999:
            batch = np.array(ar[i*batchsize:,:])
        else:
            batch = np.array(ar[i*batchsize:(i+1)*batchsize,:])
        
        mask = np.isnan(batch)

        index = np.where(mask==True)
        batch[index[0],index[1]] = 0

        neig = NearestNeighbors(n_neighbors=5, algorithm="ball_tree").fit(batch)

        for _, j in enumerate(index[0]):
            d, pos = neig.kneighbors([batch[j]])
            pos = pos[0]
            for a in range(1,5):
                if batch[pos[a],index[1][_]] != 0:
                    batch[j,index[1][_]] = batch[pos[a],index[1][_]]
        
        if i == 999:
            ar[i*batchsize:,:] = batch
        else:
            ar[i*batchsize:(i+1)*batchsize,:] = batch

    for _,i in enumerate(nas):
        name = event[0][i]
        plt.hist(ar[:,_],20)
        plt.savefig('Figures/knn_%s_%d.png'%(name,database_id))
        plt.close()

```