from keras_segmentation.models.fcn import fcn_32

model = fcn_32(n_classes=2,  input_height=360, input_width=398)

# model.train(
#     train_images="datasetfinal/image_train",
#     train_annotations="datasetfinal/image_train_annotation",
#     checkpoints_path="tmp/fcn_32", epochs=10, auto_resume_checkpoint=True
# )

# out = model.predict_segmentation(
#     inp="datasetfinal/image_test/malignant_4.png",
#     out_fname="tmp/out.png"
# )

# import matplotlib.pyplot as plt
# plt.imshow(out)

# evaluating the model

model.predict_multiple(inp_dir="datasetfinal/image_test",
                       out_dir="tmp", checkpoints_path="tmp\\fcn")

print(model.evaluate_segmentation(
    checkpoints_path="tmp/fcn_32",
    inp_images_dir="datasetfinal/image_test" ,annotations_dir="datasetfinal/image_test_annotation",))
