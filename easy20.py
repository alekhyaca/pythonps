# Create Function that will take one parameter and return type of the data. Input:500 Output:Integer Input:Coding Output:String
def get_data_type(value):
    type_map = {
        int: "Integer",
        str: "String",
        float: "Float",
        bool: "Boolean",
        list: "List",
        dict: "Dictionary",
        tuple: "Tuple",
        set: "Set",
        type(None): "NoneType"
    }
    return type_map.get(type(value), "Unknown")
print(get_data_type("alekhya"))
print(get_data_type(100))