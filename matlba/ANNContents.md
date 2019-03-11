## MATLAB 与神经网络相关的函数总结如下：
```
   nnstart - 神经网络启动GUI 
    nctool - 神经网络分类工具 
    nftool - 神经网络的拟合工具 
    nntraintool - 神经网络的训练工具 
    nprtool - 神经网络模式识别工具 
    ntstool - NFTool神经网络时间序列的工具 
    nntool - 神经网络工具箱的图形用户界面。 
    查看 - 查看一个神经网络。 
  
  网络的建立功能
    cascadeforwardnet - 串级，前馈神经网络。 
    competlayer - 竞争神经层。 
    distdelaynet - 分布时滞的神经网络。 
    elmannet - Elman神经网络。 
    feedforwardnet - 前馈神经网络。 
    fitnet - 函数拟合神经网络。 
    layrecnet - 分层递归神经网络。 
    linearlayer - 线性神经层。 
    lvqnet - 学习矢量量化（LVQ）神经网络。 
    narnet - 非线性自结合的时间序列网络。 
    narxnet - 非线性自结合的时间序列与外部输入网络。 
    newgrnn - 设计一个广义回归神经网络。 
    newhop - 建立经常性的Hopfield网络。 
    newlind - 设计一个线性层。 
    newpnn - 设计概率神经网络。 
    newrb - 径向基网络设计。 
    newrbe - 设计一个确切的径向基网络。 
    patternnet - 神经网络模式识别。 
    感知 - 感知。 
    selforgmap - 自组织特征映射。 
    timedelaynet - 时滞神经网络。 
  
  利用网络
    网络 - 创建一个自定义神经网络。 
    SIM卡 - 模拟一个神经网络。 
    初始化 - 初始化一个神经网络。 
    适应 - 允许一个神经网络来适应。 
    火车 - 火车的神经网络。 
    DISP键 - 显示一个神经网络的属性。 
    显示 - 显示的名称和神经网络属性 
    adddelay - 添加延迟神经网络的反应。 
    closeloop - 神经网络的开放反馈转换到关闭反馈回路。 
    formwb - 表格偏见和成单个向量的权重。 
    getwb - 将它作为一个单一向量中的所有网络权值和偏差。 
    noloop - 删除神经网络的开放和关闭反馈回路。 
    开环 - 转换神经网络反馈，打开封闭的反馈循环。 
    removedelay - 删除延迟神经网络的反应。 
    separatewb - 独立的偏见和重量/偏置向量的权重。 
    setwb - 将所有与单个矢量网络权值和偏差。 
  
  Simulink的支持
    gensim - 生成Simulink模块来模拟神经网络。 
    setsiminit - 集神经网络的Simulink模块的初始条件 
    getsiminit - 获取神经网络Simulink模块的初始条件 
    神经元 - 神经网络Simulink的模块库。 
 
    trainb - 批具有重量与偏见学习规则的培训。 
    trainbfg - 的BFGS拟牛顿倒传递。 
    trainbr - 贝叶斯规则的BP算法。 
    trainbu - 与重量与偏见一批无监督学习规则的培训。 
    trainbuwb - 与体重无监督学习规则与偏见一批培训。 
    trainc - 循环顺序重量/偏见的培训。 
    traincgb - 共轭鲍威尔比尔重新启动梯度反向传播。 
    traincgf - 共轭弗莱彻-里夫斯更新梯度反向传播。 
    traincgp - 共轭波拉克- Ribiere更新梯度反向传播。 
    traingd - 梯度下降反向传播。 
    traingda - 具有自适应LR的反向传播梯度下降。 
    traingdm - 与动量梯度下降。 
    traingdx - 梯度下降瓦特/惯性与自适应LR的反向传播。 
    trainlm - 采用Levenberg -马奎德倒传递。 
    trainoss - 一步割线倒传递。 
    trainr - 随机重量/偏见的培训。 
    trainrp - RPROP反向传播。 
    trainru - 无监督随机重量/偏见的培训。 
    火车 - 顺序重量/偏见的培训。 
    trainscg - 规模化共轭梯度BP算法。 
  
  绘图功能
    plotconfusion - 图分类混淆矩阵。 
    ploterrcorr - 误差自相关时间序列图。 
    ploterrhist - 绘制误差直方图。 
    plotfit - 绘图功能适合。 
    plotinerrcorr - 图输入错误的时间序列的互相关。 
    plotperform - 小区网络性能。 
    plotregression - 线性回归情节。 
    plotresponse - 动态网络图的时间序列响应。 
    plotroc - 绘制受试者工作特征。 
    plotsomhits - 小区自组织图来样打。 
    plotsomnc - 小区自组织映射邻居的连接。 
    plotsomnd - 小区自组织映射邻居的距离。 
    plotsomplanes - 小区自组织映射重量的飞机。 
    plotsompos - 小区自组织映射重量立场。 
    plotsomtop - 小区自组织映射的拓扑结构。 
    plottrainstate - 情节训练状态值。 
    plotwb - 图寒春重量和偏差值图。 
  
  列出其他神经网络实现的功能
    nnadapt - 适应职能。 
    nnderivati​​ve - 衍生功能。 
    nndistance - 距离函数。 
    nndivision - 除功能。 
    nninitlayer - 初始化层功能。 
    nninitnetwork - 初始化网络功能。 
    nninitweight - 初始化权函数。 
    nnlearn - 学习功能。 
    nnnetinput - 净输入功能。 
    nnperformance - 性能的功能。 
    nnprocess - 处理功能。 
    nnsearch - 线搜索功能。 
    nntopology - 拓扑结构的功能。 
    nntransfer - 传递函数。 
    nnweight - 重量的功能。 
    nndemos - 神经网络工具箱的示威。 
    nndatasets - 神经网络工具箱的数据集。 
    nntextdemos - 神经网络设计教科书的示威。 
    nntextbook - 神经网络设计教科书的资讯。 
 
--------------------- 
原文：https://blog.csdn.net/xgxyxs/article/details/53265318 

```
