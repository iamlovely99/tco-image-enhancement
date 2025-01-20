# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from .base_options import BaseOptions


class TestOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)
        self.parser.add_argument("--ntest", type=int, default=float("inf"), help="# of test examples.")
        self.parser.add_argument("--results_dir", type=str, default="Global/results/", help="saves results here.")
        self.parser.add_argument(
            "--aspect_ratio", type=float, default=1.0, help="aspect ratio of result images"
        )
        self.parser.add_argument("--phase", type=str, default="test", help="train, val, test, etc")
        self.parser.add_argument(
            "--which_epoch",
            type=str,
            default="latest",
            help="which epoch to load? set to latest to use latest cached model",
        )
        self.parser.add_argument("--how_many", type=int, default=50, help="how many test images to run")
        self.parser.add_argument(
            "--cluster_path",
            type=str,
            default="features_clustered_010.npy",
            help="the path for clustered results of encoded features",
        )
        self.parser.add_argument(
            "--use_encoded_image",
            action="store_true",
            help="if specified, encode the real image to get the feature map",
        )
        self.parser.add_argument("--export_onnx", type=str, help="export ONNX model to a given file")
        self.parser.add_argument("--engine", type=str, help="run serialized TRT engine")
        self.parser.add_argument("--onnx", type=str, help="run ONNX model via TRT")
        self.parser.add_argument(
            "--start_epoch",
            type=int,
            default=-1,
            help="write the start_epoch of iter.txt into this parameter",
        )

        self.parser.add_argument("--test_dataset", type=str, default="Real_RGB_old.bigfile")
        self.parser.add_argument(
            "--no_degradation",
            action="store_true",
            help="when train the mapping, enable this parameter --> no degradation will be added into clean image",
        )
        self.parser.add_argument(
            "--no_load_VAE",
            action="store_true",
            help="when train the mapping, enable this parameter --> random initialize the encoder an decoder",
        )
        self.parser.add_argument(
            "--use_v2_degradation",
            action="store_true",
            help="enable this parameter --> 4 kinds of degradations will be used to synthesize corruption",
        )
        self.parser.add_argument("--use_vae_which_epoch", type=str, default="latest")
        self.isTrain = False

        self.parser.add_argument("--generate_pair", action="store_true")

        self.parser.add_argument("--multi_scale_test", type=float, default=0.5)
        self.parser.add_argument("--multi_scale_threshold", type=float, default=0.5)
        self.parser.add_argument(
            "--mask_need_scale",
            action="store_true",
            help="enable this param meas that the pixel range of mask is 0-255",
        )
        self.parser.add_argument("--scale_num", type=int, default=1)

        self.parser.add_argument(
            "--save_feature_url", type=str, default="", help="While extracting the features, where to put"
        )

        self.parser.add_argument(
            "--test_input", type=str, default="", help="A directory or a root of bigfile"
        )
        self.parser.add_argument("--test_mask", type=str, default="", help="A directory or a root of bigfile")
        self.parser.add_argument("--test_gt", type=str, default="", help="A directory or a root of bigfile")

        self.parser.add_argument(
            "--scale_input", action="store_true", help="While testing, choose to scale the input firstly"
        )

        self.parser.add_argument(
            "--save_feature_name", type=str, default="features.json", help="The name of saved features"
        )
        self.parser.add_argument(
            "--test_rgb_old_wo_scratch", action="store_true", help="Same setting with origin test"
        )

        self.parser.add_argument("--test_mode", type=str, default="Crop", help="Scale|Full|Crop")
        self.parser.add_argument("--Quality_restore", action="store_true", help="For RGB images")
        self.parser.add_argument(
            "--Scratch_and_Quality_restore", action="store_true", help="For scratched images"
        )
        self.parser.add_argument("--HR", action='store_true',help='Large input size with scratches')

    def initializeOptions(self):
        BaseOptions.initializeOptions(self)
        self.config["ntest"] = float("inf") #help="# of test examples.")
        self.config["results_dir"] = "Global/results/" #help="saves results here.")
        self.config["aspect_ratio"] = 1.0 #help="aspect ratio of result images"
        self.config["phase"] = "test" #help="train, val, test, etc")
        self.config["which_epoch"] = "latest"
            #help="which epoch to load? set to latest to use latest cached model",
        self.config["how_many"] = 50 #help="how many test images to run")
        self.config["cluster_path"] = "features_clustered_010.npy"
            #help="the path for clustered results of encoded features",
        self.config["use_encoded_image"] = False
            # action="store_true",
            #help="if specified, encode the real image to get the feature map",
        self.config["export_onnx"] = None #help="export ONNX model to a given file")
        self.config["engine"] = None #help="run serialized TRT engine")
        self.config["onnx"] = None #help="run ONNX model via TRT")
        self.config["start_epoch"] = -1
            #help="write the start_epoch of iter.txt into this parameter",

        self.config["test_dataset"] = "Real_RGB_old.bigfile"
        self.config["no_degradation"] = False
            # action="store_true",
            #help="when train the mapping, enable this parameter --> no degradation will be added into clean image",
        self.config["no_load_VAE"] = False
            # action="store_true",
            #help="when train the mapping, enable this parameter --> random initialize the encoder an decoder",
        self.config["use_v2_degradation"] = False
            #help="enable this parameter --> 4 kinds of degradations will be used to synthesize corruption",
        self.config["use_vae_which_epoch"] = "latest"
        # self.config["isTrain"] = False
        self.isTrain = False

        self.config["generate_pair"] = False

        self.config["multi_scale_test"] = 0.5
        self.config["multi_scale_threshold"] = 0.5
        self.config["mask_need_scale"] = False
            #help="enable this param meas that the pixel range of mask is 0-255",
        self.config["scale_num"] = 1

        self.config["save_feature_url"] = "" #help="While extracting the features, where to put"

        self.config["test_input"] = "" #help="A directory or a root of bigfile"
        self.config["test_mask"] = "" #help="A directory or a root of bigfile")
        self.config["test_gt"] = "" #help="A directory or a root of bigfile")

        self.config["scale_input"] = False #help="While testing, choose to scale the input firstly"

        self.config["save_feature_name"] = "features.json" #help="The name of saved features"
        self.config["test_rgb_old_wo_scratch"] = False #help="Same setting with origin test"

        self.config["test_mode"] = "Crop" #help="Scale|Full|Crop")
        self.config["Quality_restore"] = False #help="For RGB images")
        self.config["Scratch_and_Quality_restore"] = False #help="For scratched images"
        self.config["HR"] = False #help='Large input size with scratches')