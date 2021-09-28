def test_accessLog(self):
    with open('C:/Users/ovonel/PycharmProjects/pythonProject9/testCaces/GenratedFile.log', 'r') as reader:
        for line in reader:
            if 'Title matched' in line:
                print("Verified log")
                break
