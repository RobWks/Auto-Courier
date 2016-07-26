M = csvread('test.csv');
map = reshape(M/100,[2250,768]);
I = mat2gray(map,[0,1]);
imwrite(I,'my_graphics_file.png','png')

