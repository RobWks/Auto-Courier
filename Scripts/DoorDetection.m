RGB = imread('/home/rob/Auto-Courier/Maps/E5/E5_Floor3-1_v4.png');
imagesc(RGB); %Plot image
[M,N] = size(RGB); %Calculate size of image in pixels
N = N/3; %Accounting for 3 values per pixel
axis equal
door_locations = [];
count = 0;


for i=1:N
    for j=1:M
        pixels = impixel(RGB,i,j); %Calculate value of pixel at location (c,r)
        if pixels(1) == 255
            door_locations = [door_locations; [i,j]];
        end
        count = count + 1;
        disp(count/(N*M))
    end
end
