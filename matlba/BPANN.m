%%基于Matlab的BP神经网络--源代码与工具箱实现
%% 清空环境变量
clc
clear
 
%% 训练数据预测数据提取及归一化
 
%下载四类语音信号
load data1 c1
load data2 c2
load data3 c3
load data4 c4
 
%四个特征信号矩阵合成一个矩阵
data(1:500,:) = c1(1:500,:);
data(501:1000,:) = c2(1:500,:);
data(1001:1500,:) = c3(1:500,:);
data(1501:2000,:) = c4(1:500,:);
 
%从1到2000产生随机数
k = rands(1,2000);
[m,n] = sort(k);
 
%%提取输入、输出数据
input= data(:,2:25);
output1= data(:,1);
 
%将输出数据由一维变为四维
for i = 1:1:2000
	switch output1(i)
		case 1 
			output(i,:) = [1 0 0 0];
		case 2
			output(i,:) = [0 1 0 0];
		case 3
			output(i,:) = [0 0 1 0];
		case 4
			output(i,:) = [0 0 0 1];
	end
end
 
%随机提取1500个测试数据，500个样本为预测数据
input_train = input(n(1:1500),:)';
output_train = output(n(1:1500),:)';
input_test = input(n(1501:2000),:)';
output_test = output(n(1501:2000),:)';
 
%归一化
[inputn,inputps] = mapminmax(input_train);
 
%变量、权值初始化
innum = 24;
midnum = 25;
outnum = 4;
 
w1 = rands(midnum,innum);
b1 = rands(midnum,1);
w2 = rands(outnum,midnum);
b2 = rands(outnum,1);
 
w1_1 = w1;
b1_1 = b1;
w2_1 = w2;
b2_1 = b2;
 
xite = 0.1
 
%%网络训练
for ii=1:10
	E(ii)=0;
	for i = 1:1500
		x = inputn(:,i);
		for j = 1:1:midnum
			%%计算隐层值
			I(j) = inputn(:,i)'*w1(j,:)' + b1(j);
			Iout(j) =1/(1+exp(-I(j)));
		end
		
		%%计算输出层值
		yn = w2*Iout' + b2;
		
		%%计算误差
		e = output_train(:,i)-yn;
		E(ii) = E(ii) + sum(abs(e));
		
		%%计算权值变化率
		dw2 = e*Iout;
		db2 = e;
		
		for j = 1:1:midnum
			S = 1/(1+exp(-I(j)));
			FI(j) = S*(1-S);
		end
		
		for k = 1:innum
			for j = 1:midnum
				dw1(j,k) = FI(j)*x(k)*(w2(:,j)'*e);
				db1(j) = FI(j)*(w2(:,j)'*e);
			end
		end
		
		%%更新权值
		w1 = w1_1 + xite*dw1;
		b1 = b1_1 + xite*db1';
		w2 = w2_1 + xite*dw2;
		b2 = b2_1 + xite*db2;
		
		w1_1 = w1;
		b1_1 = b1;
		w2_1 = w2;
		b2_1 = b2;
	end
end
 
%%语音信号分类
inputn_test = mapminmax('apply',input_test,inputps);
 
for i=1:1:500
	for j = 1:1:midnum
		I(j) = inputn_test(:,i)'*w1(j,:)' + b1(j);
		Iout(j) = 1/(1+exp(-I(j)));
	end
	
	fore(:,i) = w2*Iout' + b2;
 
end
 
%%计算误差
for i =1:1:500
	output_fore(i) = find(fore(:,i) == max(fore(:,i)));
end
	
error =output_fore - output1(n(1501:2000))';
%画出预测语音种类和实际语音种类的分类图
figure(1)
plot(output_fore,'r')
hold on
plot(output1(n(1501:2000))','b')
legend('预测语音类别','实际语音类别')
 
%画出误差图
figure(2)
plot(error)
title('BP网络分类误差','fontsize',12)
xlabel('语音信号','fontsize',12)
ylabel('分类误差','fontsize',12)
 
%print -dtiff -r600 1-4
 
k=zeros(1,4);  
%找出判断错误的分类属于哪一类
for i=1:1:500
	if error(i)~=0
		[b,c]=max(output_test(:,i));
		switch c
			case 1 
                k(1) = k(1) +1;
			case 2 
                k(2) = k(2) +1;
			case 3
                k(3) = k(3) +1;
			case 4
                k(4) = k(4) +1;
		end
	end
end
				
%找出每类的个体和
kk=zeros(1,4);
for i=1:500
    [b,c]=max(output_test(:,i));
    switch c
        case 1
            kk(1)=kk(1)+1;
        case 2
            kk(2)=kk(2)+1;
        case 3
            kk(3)=kk(3)+1;
        case 4
            kk(4)=kk(4)+1;
    end
end
radio = (kk-k)./kk
--------------------- 
作者：兔美酱xz 
来源：CSDN 
原文：https://blog.csdn.net/xz_rabbit/article/details/20399659 
版权声明：本文为博主原创文章，转载请附上博文链接！
