from lxml import etree

def validar_con_xsd(xml_file, xsd_file):
    try:
        with open(xml_file, 'rb') as xml_file, open(xsd_file, 'rb') as xsd_file:
            xml_tree = etree.parse(xml_file)
            xsd = etree.XMLSchema(etree.parse(xsd_file))
            
            if xsd.validate(xml_tree):
                print("El documento XML es válido según el esquema XSD.")
            else:
                print("El documento XML no es válido según el esquema XSD.")
                print(xsd.error_log)

    except Exception as e:
        print(f"Error al validar el documento: {e}")

validar_con_xsd("restaurantxsd.xml", "restaurant.xsd")
