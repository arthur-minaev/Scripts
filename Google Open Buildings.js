var ds = ee.FeatureCollection("projects/sat-io/open-datasets/VIDA_COMBINED/RUS");
var bounds = "projects/minaev-99/assets/russia_new_regions"; // set directory for input boundaries
var region = 'Нижегородская область'; // select interested region
var desc = 'Buildings_NN'; // set description for selected region
var folder = 'FILES'; // set directory on your Google Drive

// get & filter data
var regions = ee.FeatureCollection(bounds);
var ds_clip = ds.filterBounds(
  regions.filter(ee.Filter.eq('locname', region))); 
ds_clip = ds_clip.map(function(f) {
  return f.set('geo_type', f.geometry().type())});
var ds_filt = ds_clip.filter(ee.Filter.eq('geo_type', 'Polygon'));
//print(rus_flt.size());
//print(rus_flt.limit(3));

// visualisation
Map.addLayer(ds_filt.style({fillColor:'00000000',color:'#FF0000'}),{},'Buildings');
Map.setOptions('satellite', {});

// export data to Google Drive
Export.table.toDrive({
    collection: ds_filt,
    description: desc, 
    folder: folder,
    selectors: ['area_in_meters','bf_source','confidence'],
    fileFormat: 'KMZ'});

// Link: https://code.earthengine.google.com/656a5ba2be6ef6d7a201bbc76aee87b3
