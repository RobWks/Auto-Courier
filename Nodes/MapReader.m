file = csvread('e5_smaller.csv');
input = reshape(file/100,[2250/2,768/2]);
map = im2bw(input,0.7);
map = flipud(map);
[M,N]= size(map);
imagesc(map);
hold on

num_obstacles = 5000;
x_o = round(rand(1,num_obstacles)*(N-1))+1;
y_o = round(rand(1,num_obstacles)*(M-1))+1;


for i=fliplr(1:length(x_o))
    if ~map(y_o(i),x_o(i))
        x_o(i) = [];
        y_o(i) = [];
    end
end

plot(x_o,y_o,'*')
axis equal
