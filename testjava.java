import java.util.HashMap;

public class Vertex {
	public HashMap<String,Integer> adj;	//A hash map that stores adjacent nodes
	String name;						//Name of the vertex (Eg: V0)
	public boolean known;				//Boolean that stores if the path is known
	public Vertex path;					//Stores the Vertex which the path goes through
	int dist;							//Distance
	//Constructor
	public Vertex(String name){
		adj = new HashMap<String,Integer>();
		dist = -1;
		known = false;
		path = null;
		this.name = name;
	}
	
	//f: Resets the values of dist, known and path for a vertex
	//This is used in 'shortestPath'
	//c: Complexity: O(1)
	public void resetVertex() {
		dist = -1;
		known = false;
		path = null;
	}
	
	//f: Copies the hash map containing the adjacent nodes.
	//c: Complexity: O(I) (where I is all edges connected to 'this')
	public HashMap<String,Integer> copyPaths() {
		HashMap<String,Integer> c = new HashMap<String,Integer>();
		for(String key: adj.keySet()) {
			c.put(key, adj.get(key));
		}	
		return c;
	}
	
	//f: Returns true if obj is equal to 'this'.
	//p: obj, the object to compare 'this' to
	//c: Complexity: O(1)
	public boolean equals(Object obj) {
		if (obj == null || !(obj instanceof Vertex)) return false;
		Vertex ver = (Vertex) obj;
		return (this == ver);
	}
}
