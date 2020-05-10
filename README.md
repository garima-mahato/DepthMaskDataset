# DepthMaskDataset


## Dataset Links

[Link to fg_bg_mask_dataset](https://drive.google.com/file/d/11TbUmMY9mYyIeRCkh5kGGIZ-k1Vbs-Qz/view?usp=sharing)

[Link to depth dataset](https://drive.google.com/open?id=1sEdl7u4VcP2dqcAR4O3VsiixNspu08RA)


## Dataset Description

### 1) Background Images

![](https://raw.githubusercontent.com/genigarus/DepthMaskDataset/master/asset/sample_bg.PNG)

Background consists of indoor office images of size 160x160.

**Size of BG data = 790.72 KB**

**Total number of images = 100**


### 2) Foreground Images

![](https://raw.githubusercontent.com/genigarus/DepthMaskDataset/master/asset/sample_fg.PNG)

Foreground consists of office furniture, people, and staff. They were created in Powerpoint by using "Background removal" option and then saving it alpha png image files.

**Size of FG data = 2.16 MB**

**Total number of images = 100**


### 3) Foreground Masks

![](https://raw.githubusercontent.com/genigarus/DepthMaskDataset/master/asset/sample_fg_mask.PNG)

Foreground masks were created in Adobe photoshop by following below steps:

1) Select magic wand and then click on the foreground image.
2) Right click and select "Invert" option.
3) In the layers panel, on right-hand side, add layer mask.
4) Select the layer mask icon on the panel, then Ctrl+A, followed by Ctrl+N and then click Ok. Then, do Ctrl+V.
5) Save the resultant image.

**Size of FG mask data = 351.34 KB**

**Total number of images = 100**


### 4) Foreground overlayed on Background

![](https://raw.githubusercontent.com/genigarus/DepthMaskDataset/master/asset/fg_bg.png)

1) All background images were cropped to square and then resized to 160x160 (and 224) using [utility](https://github.com/genigarus/DepthMaskDataset/blob/master/utility.py). 

2) All foreground and their mask images were cropped and then rescaled to 150 (and 200)   using [utility](https://github.com/genigarus/DepthMaskDataset/blob/master/utility.py).

3) For each background, I ran a loop for each fg. Within the loop, each fg was taken and flipped. Then, for each of fg and its flip, randomly selected x and y position within fg range. Also, tried scaling. Taking these position, pasted the the fg on bg at those positions and **its fg mask on black bg**.

4) [Link to file](https://github.com/genigarus/DepthMaskDataset/blob/master/OverlayingForegroundOnBackground.ipynb)

5) These images were stored in zip file. It took around 2.5 hours.

**For FG_BG data:-
Mean is (1.0, 1.0, 1.0)**

**Std is (0.21974199573317058, 0.228182355952634, 0.24135464023694234)**

**Total number of images = 400000**


**Size of FG_BG and its mask compressed file = 1.49 GB**


### 5) Mask of Foreground overlayed on Background

![](https://raw.githubusercontent.com/genigarus/DepthMaskDataset/master/asset/fg_bg_mask.png)

As explained above.

**For FG_BG_MASK data:-
Mean is 0.0**

**Std is 0.3169699513813231**

**Total number of images = 400000**

### 6) Depth map of Foreground overlayed on Background

![](https://raw.githubusercontent.com/genigarus/DepthMaskDataset/master/asset/sample_depth_map.PNG)

1) For depth map, Loaded the DenseDepth model with "nyu.h5" weights.

2) Read the data from zipfile. 

3) Broke the entire task into batch of 100.

4) Then, tested which batch size gave better results in terms of time and memory for 1 batch. **Batch size 32 gave better results**

5) For each batch consisting of 4000 images, The model was used for prediction with batch size 32. Then, the outputs were saved as numpy compressed file(npz). So, for 100 batches, it took around 3 hours in comparison to 12 hours if I was saving it in zipfile.

6) Then the data from npz files were used to generate images. This is partially completed and is in progress. 

7) [Link](https://github.com/genigarus/DepthMaskDataset/blob/master/DepthMapGeneration.ipynb)

**For Depth map data:-
Mean is 0.0**

**Std is 0.03913845191709697**

**Total number of images = 400000**

**Size of depthmap compressed file = 7.78 GB (of npz files)**

## Data Statistics

[Link](https://github.com/genigarus/DepthMaskDataset/blob/master/DepthMaskDatasetStatistics.ipynb)


**Total Dataset Size = 9.27 GB (including all 6 types of images above)**
