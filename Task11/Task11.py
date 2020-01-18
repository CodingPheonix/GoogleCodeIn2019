import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#Singapore

singaporeNatural=gpd.read_file('singapore/natural.shp')
singaporeRoads=gpd.read_file('singapore/roads.shp')
singaporeWaterways=gpd.read_file('singapore/waterways.shp')
singaporeRailways=gpd.read_file('singapore/railways.shp')

fig = plt.subplots()[0]

naturePatch = mpatches.Patch(color='green', label='Land')
roadPatch = mpatches.Patch(color='grey', label='Road')
waterwayPatch = mpatches.Patch(color='blue', label='Waterway')
railwayPatch = mpatches.Patch(color='purple', label='Railway')

fig.legend(handles=[naturePatch, roadPatch, waterwayPatch, railwayPatch], loc = 'lower center', ncol=5, labelspacing=0. )

axes = []
axes.append(plt.subplot2grid(shape=(2,6), loc=(0,0), colspan=2))
axes.append(plt.subplot2grid((2,6), (0,2), colspan=2))
axes.append(plt.subplot2grid((2,6), (0,4), colspan=2))
axes.append(plt.subplot2grid((2,6), (1,1), colspan=2))
axes.append(plt.subplot2grid((2,6), (1,3), colspan=2))

for ax in axes:
    ax.set_xticks([])
    ax.set_yticks([])

naturalPatch = mpatches.Patch(color='green', label='Land')
roadPatch = mpatches.Patch(color='grey', label='Roads')
waterwayPatch = mpatches.Patch(color='blue', label='Waterways')
railwayPatch = mpatches.Patch(color='purple', label='Railways')

fig.suptitle('Maps of 5 cities', fontsize=25, fontweight='bold', y=0.925)

axes[0].set_title('Map of Singapore')

singaporeNatural.plot(ax=axes[0], color='green', zorder=0)
singaporeRoads.plot(ax=axes[0], color='grey', zorder=1)
singaporeWaterways.plot(ax=axes[0], color='blue', zorder=2)
singaporeRailways.plot(ax=axes[0], color='purple', zorder=3)

#Paris

parisNatural=gpd.read_file('paris/natural.shp')
parisRoads=gpd.read_file('paris/roads.shp')
parisWaterways=gpd.read_file('paris/waterways.shp')
parisRailways=gpd.read_file('paris/railways.shp')

axes[1].set_title('Map of Paris')

parisNatural.plot(ax=axes[1], color='green', zorder=0)
parisRoads.plot(ax=axes[1], color='grey', zorder=1)
parisWaterways.plot(ax=axes[1], color='blue', zorder=2)
parisRailways.plot(ax=axes[1], color='purple', zorder=3)

#Syndey

sydneyNatural=gpd.read_file('sydney/natural.shp')
sydneyRoads=gpd.read_file('sydney/roads.shp')
sydneyWaterways=gpd.read_file('sydney/waterways.shp')
sydneyRailways=gpd.read_file('sydney/railways.shp')

axes[2].set_title('Map of Sydney')

sydneyNatural.plot(ax=axes[2], color='green', zorder=0)
sydneyRoads.plot(ax=axes[2], color='grey', zorder=1)
sydneyWaterways.plot(ax=axes[2], color='blue', zorder=2)
sydneyRailways.plot(ax=axes[2], color='purple', zorder=3)

#London

londonNatural=gpd.read_file('london/natural.shp')
londonRoads=gpd.read_file('london/roads.shp')
londonWaterways=gpd.read_file('london/waterways.shp')
londonRailways=gpd.read_file('london/railways.shp')

axes[3].set_title('Map of London')

londonNatural.plot(ax=axes[3], color='green', zorder=0)
londonRoads.plot(ax=axes[3], color='grey', zorder=1)
londonWaterways.plot(ax=axes[3], color='blue', zorder=2)
londonRailways.plot(ax=axes[3], color='purple', zorder=3)

#Bankok

bankokNatural=gpd.read_file('bankok/natural.shp')
bankokRoads=gpd.read_file('bankok/roads.shp')
bankokWaterways=gpd.read_file('bankok/waterways.shp')
bankokRailways=gpd.read_file('bankok/railways.shp')

axes[4].set_title('Map of Bankok')

bankokNatural.plot(ax=axes[4], color='green', zorder=0)
bankokRoads.plot(ax=axes[4], color='grey', zorder=1)
bankokWaterways.plot(ax=axes[4], color='blue', zorder=2)
bankokRailways.plot(ax=axes[4], color='purple', zorder=3)

#Show

plt.show() 
