import jinja2 as j2
import tile_gen.vectiles.transform as transform
import tile_gen.vectiles.sort as sort

def get_module(env, template_name):
    return env.get_template(template_name).module

queries_env = j2.Environment(loader=j2.PackageLoader('queries', ''))
roads = get_module(queries_env, 'roads.jinja2').roads
earth = get_module(queries_env, 'earth.jinja2').earth
water = get_module(queries_env, 'water.jinja2').water

config = {"dbinfo": {"user": "zoonmaps",
                     "database": "gis"},
          "layers": {"roads": {"query_fn": roads,
                               "geometry_types": ["LineString", "MultiLineString"],
                               "transform_fns": [transform.add_id_to_properties,
                                                 transform.detect_osm_relation,
                                                 transform.road_kind,
                                                 transform.road_classifier,
                                                 transform.road_sort_key,
                                                 transform.road_oneway,
                                                 transform.road_trim_properties,
                                                 transform.remove_feature_id],
                               "sort_fn": sort.roads},

                     "earth": {"query_fn": earth,
                               "simplify": 0,
                               "geometry_types": ["Polygon", "MultiPolygon"],
                               "transform_fns": [transform.add_id_to_properties,
                                                 transform.detect_osm_relation,
                                                 transform.remove_feature_id],
                               "sort_fn": sort.earth},
                     "water": {"query_fn": water,
                               "simplify": 0,
                               "geometry_types": ["Polygon",
                                                  "MultiPolygon",
                                                  "LineString",
                                                  "MultiLineString"],
                               "transform_fns": [transform.add_id_to_properties,
                                                 transform.detect_osm_relation,
                                                 transform.remove_feature_id],
                               "sort_fn": sort.water}}}

'''


                     "boundaries": {"queries": [],
                                    "simplify": 0,
                                    "geometry_types": ["LineString", "MultiLineString"],
                                    "transform_fns": [transform.add_id_to_properties,
                                                      transform.detect_osm_relation,
                                                      transform.remove_feature_id]}
'''