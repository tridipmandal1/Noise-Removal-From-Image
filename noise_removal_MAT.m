%loading an image
y =imread('WhatsApp Image 2023-12-05 at 20.07.36_679d46d9.jpg');
imshow(y);
clc;
close all;
clear all;
z=imread('WhatsApp Image 2023-12-05 at 20.07.36_679d46d9.jpg');
p=rgb2gray(z);
p1=imnoise(p,'salt & pepper', 0.4);
h1=1/9*ones(3,3);
h2=1/25*ones(5,5);
c1=conv2(p1,h1,'same');
c2=conv2(p1,h2,'same');

m1=medfilt2(p1,[3 3]);
m2=medfilt2(p1,[9 9]);

figure;
subplot(2,3,1);imshow(p);title('Original Image');
subplot(2,3,2);imshow(c1,[]);title('Mean Filtered Image 1');
subplot(2,3,3);imshow(c2,[]);title('Mean Filtered Image 2');
subplot(2,3,4);imshow(p1);title('Noisy Image');
subplot(2,3,5);imshow(m1);title('Median Filtered Image 1');
subplot(2,3,6);imshow(m2);title('Median Filtered Image 2');