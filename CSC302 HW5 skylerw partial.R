library(ggplot2) #visualization library
require(maps)
require(mapdata)
library(sf)
install.packages('sf')

load('/Users/skyler/Downloads/Slides13_Geo_Rscripts_Data/US_states_geoms.rda')
load('/Users/skyler/Downloads/Slides13_Geo_Rscripts_Data/wind_turbines.rda')

california <- map_data("state")
head(california$region)
brown <- "#deb664"

temp <- wind_turbines
wind_ca <- temp$t_state=='CA'

ggplot(california$region=california) + 
  geom_sf(fill = brown, color = "black", size = 0.5/.pt) +
  coord_sf(datum = NA, expand = FALSE) +
  theme(
    plot.margin = margin(6, 6, 1, 1.5) 
  )
