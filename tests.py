import traceback
from flask import jsonify

try:
	from main import app
	import unittest
except Exception as e:
	print("Error while importing modules: {}".format(traceback.print_exc(e)))


class getrefTests(unittest.TestCase):
	# test for homepage response
	def test_homepage(self):
		tester = app.test_client(self)
		response = tester.get("/")
		status = response.status_code
		self.assertEqual(status, 200)

	# test api response status 200
	def test_getref(self):
		tester = app.test_client(self)
		response = tester.get("/get_ref/3050107579885e1608e6fe50fae3f8d0")
		status = response.status_code
		self.assertEqual(status, 200)

	# test api response status 404
	def test_getref_404(self):
		tester = app.test_client(self)
		response = tester.get("/get_ref/")
		status = response.status_code
		self.assertEqual(status, 404)

	# test api response datatype
	def test_getref_datatype(self):
		tester = app.test_client(self)
		response = tester.get("/get_ref/3050107579885e1608e6fe50fae3f8d0")
		content_type = response.content_type
		self.assertEqual(content_type, "application/json")

	# test api response contents
	def test_getref_content(self):
		tester = app.test_client(self)
		response = tester.get("/get_ref/3050107579885e1608e6fe50fae3f8d0")
		self.assertTrue(b'metadata' in response.data)
		self.assertTrue(b'aliases' in response.data)
		self.assertTrue(b'id' in response.data)
		self.assertTrue(b'length' in response.data)
		self.assertTrue(b'length' in response.data)
		self.assertTrue(b'length' in response.data)

if __name__ == "__main__":
	unittest.main()