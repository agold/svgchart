from xml.etree.ElementTree import *
import xml.etree.ElementTree as etree

# This is a terrible hack to add CDATA serialization to ElementTree.
# It allows serialization of CDATA sections at the expense of comments.
# Any comments will be rendered as CDATA sections due to this
# This was necessary because ElementTree makes explicit exceptions
# at several points for handling comments, which makes it very difficult
# to add a CDATA handler. Hopefully ElementTree will natively support CDATA
# in the future, at which point I can retire this patch.
old_serialize_xml = etree._serialize_xml
def cdata_serialize_xml(write, elem, encoding, qnames, namespaces):
	"""This is a terrible hack to add CDATA serialization to ElementTree.
	It allows serialization of CDATA sections at the expense of comments.
	Any comments will be rendered as CDATA sections due to this
	This was necessary because ElementTree makes explicit exceptions
	at several points for handling comments, which makes it very difficult
	to add a CDATA handler. Hopefully ElementTree will natively support CDATA
	in the future, at which point I can retire this patch.
	"""
	tag = elem.tag
	text = elem.text
	if tag is etree.Comment:
		write("<![CDATA[%s]]>" % etree._encode(text, encoding))
		return
	else:
		old_serialize_xml(write, elem, encoding, qnames, namespaces)
etree._serialize_xml = cdata_serialize_xml
