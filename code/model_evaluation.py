dir_aso = './data/ASO/ASO_3M_SD_USCATE_20180528_clip.tif'
raso = rasterio.open(dir_aso,'r').read()
raso = np.where(raso[0,:,:] < 0, np.nan, raso)

th = 0.1 # using 10 cm threshold
raso_binary = np.where(raso >= 0.1, 1, 0) # if the SD is higher than 10 cm, then snow; otherwise, no-snow

fig, axs = plt.subplots(1,2,figsize=(16,6))
im1 = axs[0].imshow(raso[0,:,:],cmap = 'Blues',vmin = 0, vmax = 5)
axs[0].set_title('ASO snow depth', fontsize=16)
fig.colorbar(im1, ax = axs[0], label = 'snow depth (meter)', extend = 'max')

im2 = axs[1].imshow(raso_binary[0,:,:], cmap = 'gray', interpolation = 'none')
axs[1].set_title('ASO snow cover (TH = 10 cm)', fontsize=16)

dir_model = "./models/random_forest_SCA_binary.joblib"
# load model
model = joblib.load(dir_model)

df = pd.DataFrame()
df['obs'] = y_test
df['predict'] = model.predict(X_test)

# Cross-tabulate predictions
print(pd.crosstab(df['obs'], df['predict'], margins=True))
print(calculate_metrics(df))

dir_raster = './data/planet/20180528_181110_1025_3B_AnalyticMS_SR_clip.tif'
dir_out = './data/SCA/'
nodata_flag = 9
run_sca_prediction(dir_raster, dir_out, nodata_flag, model)

dir_planet = './data/planet/20180528_181110_1025_3B_AnalyticMS_SR_clip.tif'
r_na_flag = rasterio.open(dir_planet, 'r').read()
r_planet = rasterio.open(dir_planet, 'r').read([4,3,2])/10000

dir_sca = './data/SCA/20180528_181110_1025_3B_AnalyticMS_SR_clip_SCA.tif'
r_sca = rasterio.open(dir_sca, 'r')

fig, (ax1, ax2) = plt.subplots(1,2, figsize = (16,4))
show(r_planet, ax= ax1, cmap='jet', interpolation = 'none',title = 'Planet false color Image')
show(r_sca.read().squeeze(), ax= ax2, interpolation = 'none',title = 'Planet Snow Cover')

dir_planet_ext = './data/GIS/extent/CATE_20180528_181110_img_ext.shp'
with fiona.open(dir_planet_ext, "r") as shapefile:
    shapes = [feature["geometry"] for feature in shapefile]
    
dir_aso = "./data/ASO/ASO_3M_SD_USCATE_20180528_binary_clip.tif"
with rasterio.open(dir_aso,'r') as src:
    r_aso = rasterio.mask.mask(src, shapes, crop=True, filled = False)
    
dir_pred = './data/SCA/20180528_181110_1025_3B_AnalyticMS_SR_clip_SCA.tif'
with rasterio.open(dir_pred,'r') as src:
    r_predict = rasterio.mask.mask(src, shapes, crop=True, filled = False)

dir_watermask = './data/mask/waterbody_TB_UTM11_clip.tif'
with rasterio.open(dir_watermask,'r') as src:
    r_watermask = rasterio.mask.mask(src, shapes, crop=True, filled = False)
    
dir_glaciermask = './data/mask/02_rgi60_WesternCanadaUS_hypso_TB_clip.tif'
with rasterio.open(dir_glaciermask,'r') as src:
    r_glaciermask = rasterio.mask.mask(src, shapes, crop=True, filled = False)
    
    
df = pd.DataFrame()
df['predict'] = r_predict[0].ravel()
df['obs'] = r_aso[0].ravel()
df['watermask'] = r_watermask[0].ravel()
df['glaciermask'] = r_watermask[0].ravel()

# remove NA data region, water bodies, and glaciers 
df_mask = df[(df.predict >= 0) & (df.watermask != 0) & (df.glaciermask != 0)]
# print(df)

print("overall model performance:")
print(calculate_metrics(df_mask))

file_landcover = './data/ASO/ASO_3M_CHM_USCATB_20140827_binary_clip.tif' # 1 - forest, 0 open area
with rasterio.open(file_landcover,'r') as src:
    r_landcover = rasterio.mask.mask(src, shapes, crop=True, filled = False)
    
df['landcover'] = r_landcover[0].ravel()

df_mask = df[(df.predict >= 0) & (df.watermask != 0) & (df.glaciermask != 0)]
df_open = df_mask[df_mask.landcover == 0]
print("Model performance in open areas:")
print(calculate_metrics(df_open))

df_forest = df_mask[df_mask.landcover == 1]
print("Model performance in forested areas:")
print(calculate_metrics(df_forest))
