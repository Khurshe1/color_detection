import argparse

ap = argparse.ArgumnetParser()

ap.add_argument('-i', '--image', required=True, help="Image Path")

#parse the command-line arguments provided by the user
args = vars(ap.parse_args())

img_path=args['image']

img = cv2.imread(img_path)

