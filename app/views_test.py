import unittest
from unittest.mock import patch

import requests as requests
from app import app


class MyTestCase(unittest.TestCase):
    body_test = {
        "date": "2020-02-01",
        "feature_1": 0,
        "feature_2": 0,
        "feature_3": 23.0,
        "feature_4": 0,
        "feature_5": 0,
        "feature_6": 21.0,
        "feature_7": 2.1973,
        "feature_8": 0,
        "feature_9": 0,
        "feature_10": 15.2739,
        "feature_11": 0,
        "feature_12": 0,
        "feature_13": 0,
        "feature_14": 0,
        "feature_15": 0,
        "feature_16": 0.5568,
        "feature_17": 0,
        "feature_18": 0,
        "feature_19": 1.0,
        "feature_20": 0,
        "feature_21": 0,
        "feature_22": 0,
        "feature_23": 17.1452,
        "feature_24": 0,
        "feature_25": 0,
        "feature_26": 57.0,
        "feature_27": 0,
        "feature_28": 0,
        "feature_29": 0,
        "feature_30": 0.6841,
        "feature_31": 0.7112,
        "feature_32": 0,
        "feature_33": 0,
        "feature_34": 41.2141,
        "feature_35": 0,
        "feature_36": 0,
        "feature_37": 42.8634,
        "feature_38": 0,
        "feature_39": 0,
        "feature_40": 9.0,
        "feature_41": 0,
        "feature_42": 0,
        "feature_43": 0,
        "feature_44": 1.2242,
        "feature_45": 13.0,
        "feature_46": 2.3638,
        "feature_47": 29.5852,
        "feature_48": 0,
        "feature_49": 1.8323,
        "feature_50": 0,
        "feature_51": 0,
        "feature_52": 70.0,
        "feature_53": 123.8373,
        "feature_54": 68.6177,
        "feature_55": 29.99,
        "feature_56": 0,
        "feature_57": 0,
        "feature_58": 0,
        "feature_59": 0,
        "feature_60": 0,
        "feature_61": 5.7495,
        "feature_62": 0,
        "feature_63": 0,
        "feature_64": 4.0,
        "feature_65": 0,
        "feature_66": 0,
        "feature_67": 0,
        "feature_68": 0,
        "feature_69": 0,
        "feature_70": 0,
        "feature_71": 0,
        "feature_72": 0,
        "feature_73": 0,
        "feature_74": 0.2151,
        "feature_75": 0,
        "feature_76": 25.3545,
        "feature_77": 0,
        "feature_78": 22.882,
        "feature_79": 0,
        "feature_80": 0,
        "feature_81": 0,
        "feature_82": 0,
        "feature_83": -11.5191,
        "feature_84": 0.7847,
        "feature_85": 0,
        "feature_86": 13.1122,
        "feature_87": 39.0,
        "feature_88": 67.0,
        "feature_89": 0,
        "feature_90": 0,
        "feature_91": 5.7868,
        "feature_92": 77.5917,
        "feature_93": 0,
        "feature_94": 0,
        "feature_95": 37.0,
        "feature_96": 0,
        "feature_97": 64.0,
        "feature_98": 51.2223,
        "feature_99": 44.0
    }
    body_test_response = {
        "prediction": "[8.496706397163543]"
    }

    # check for the response case when the request is, malformed
    def test_home(self):
        tester = app.test_client()
        response = tester.post("http://192.168.100.2:5000/predict")
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

    # test the type of the response value
    # 'text/html; charset=utf-8', since i did not specify the content_type
    def test_index_content1(self):
        tester = app.test_client()
        response = tester.post("http://192.168.100.2:5000/predict")
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

    def test_index_content2(self):
        tester = app.test_client()
        response = tester.post("http://192.168.100.2:5000/predict")
        self.assertIsNot(response.content_type, 'Application/json')

    # test the response code for a right request
    def test_index_data_response_code(self):
        response = requests.post("http://192.168.100.2:5000/predict", json=self.body_test)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.json(), self.body_test_response)

    # test the response value for a right request
    def test_index_data_response_data(self):
        response = requests.post("http://192.168.100.2:5000/predict", json=self.body_test)
        self.assertEqual(response.json(), self.body_test_response)


if __name__ == '__main__':
    unittest.main()
