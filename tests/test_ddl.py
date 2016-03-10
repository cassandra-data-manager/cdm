from pytest import fixture
from cdm.ddl import parse_line, create_vertex, create_vertex_index,\
                    CreateVertex, \
                    CreateEdge, CreateProperty, CreateIndex, CreateGraph


def test_create_graph():
    s = "CREATE GRAPH jon"
    parsed = parse_line(s)
    assert isinstance(parsed, CreateGraph)
    assert "system.createGraph('jon').build()" in str(parsed)

def test_create_vertex_label():
    cmd = "CREATE vertex movie"
    result = create_vertex.parseString(cmd)[0]
    assert isinstance(result, CreateVertex)

    result = parse_line(cmd)
    assert isinstance(result, CreateVertex)
    assert result.label == "movie"

    assert "buildVertexLabel" in str(result)
    assert "movie" in str(result)

    result2 = parse_line("CREATE vertex label movie")
    assert isinstance(result, CreateVertex)

def test_create_edge_label():
    result = parse_line("CREATE edge rated")
    assert isinstance(result, CreateEdge)
    assert result.label == "rated"
    result2 = parse_line("CREATE edge label rated")
    assert isinstance(result2, CreateEdge)



def test_create_property():
    result = parse_line("CREATE PROPERTY name text")
    assert isinstance(result, CreateProperty)
    result = parse_line("CREATE PROPERTY name TEXT")
    assert isinstance(result, CreateProperty)


"""
graph.schema().vertexLabel("ip").buildVertexIndex("ipById").materialized().byPropertyKey("id").add()
Secondary
graph.schema().vertexLabel("ip").buildVertexIndex("ipByCountry").secondary().byPropertyKey("country").add()
Search
graph.schema().vertexLabel("swid").buildVertexIndex("search").search().byPropertyKey("dob").add()
"""

def test_create_index_fulltext():
    s = "CREATE materialized INDEX movie_title_idx ON VERTEX movie(title )"
    result = create_vertex_index.parseString(s)[0]
    assert result.type == "materialized"

    s = "CREATE secondary INDEX movie_title_idx ON VERTEX movie(title )"
    result = create_vertex_index.parseString(s)[0]
    assert result.type == "secondary"


#     result = parse_line()
#     assert isinstance(result, CreateIndex)
#
# def test_create_index_materialize():
#     result = parse_line("CREATE INDEX movie_title_idx ON movie(title) SEARCH");
#     result = parse_line("CREATE INDEX user_id_idx ON movie(user_id) MATERIALIZED")
