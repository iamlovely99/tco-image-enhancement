def initializeOptions(self):
        BaseOptions.initializeOptions(self)
        self.config["ntest"] = float("inf") #help="# of test examples.")
        self.config["results_dir"] = "./results/" #help="saves results here.")
        self.config["aspect_ratio"] = 1.0 #help="aspect ratio of result images"
        self.config["phase"] = "test" #help="train, val, test, etc")
        self.config["which_epoch"] = "latest"
            #help="which epoch to load? set to latest to use latest cached model",
        self.config["how_many"] = 50, #help="how many test images to run")
        self.config["cluster_path"] = "features_clustered_010.npy"
            #help="the path for clustered results of encoded features",
        self.config["use_encoded_image"] = True
            # action="store_true",
            #help="if specified, encode the real image to get the feature map",
        self.config["export_onnx"] = "" #help="export ONNX model to a given file")
        self.config["engine"] = "" #help="run serialized TRT engine")
        self.config["onnx"] = "" #help="run ONNX model via TRT")
        self.config["start_epoch"] = -1
            #help="write the start_epoch of iter.txt into this parameter",

        self.config["test_dataset"] = "Real_RGB_old.bigfile"
        self.config["no_degradation"] = True
            # action="store_true",
            #help="when train the mapping, enable this parameter --> no degradation will be added into clean image",
        self.config["no_load_VAE"] = True
            # action="store_true",
            #help="when train the mapping, enable this parameter --> random initialize the encoder an decoder",
        self.config["use_v2_degradation"] = True
            #help="enable this parameter --> 4 kinds of degradations will be used to synthesize corruption",
        self.config["use_vae_which_epoch"] = "latest"
        self.isTrain = False

        self.config["generate_pair"] = True

        self.config["multi_scale_test"] = 0.5
        self.config["multi_scale_threshold"] = 0.5
        self.config["mask_need_scale"] = True
            #help="enable this param meas that the pixel range of mask is 0-255",
        self.config["scale_num"] = 1

        self.config["save_feature_url"] = "" #help="While extracting the features, where to put"

        self.config["test_input"] = "" #help="A directory or a root of bigfile"
        self.config["test_mask"] = "" #help="A directory or a root of bigfile")
        self.config["test_gt"] = "" #help="A directory or a root of bigfile")

        self.config["scale_input"] = True #help="While testing, choose to scale the input firstly"

        self.config["save_feature_name"] = "features.json" #help="The name of saved features"
        self.config["test_rgb_old_wo_scratch"] = True #help="Same setting with origin test"

        self.config["test_mode"] = "Crop", #help="Scale|Full|Crop")
        self.config["Quality_restore"] = True #help="For RGB images")
        self.config["Scratch_and_Quality_restore"] = True #help="For scratched images"
        self.config["HR"] = True #help='Large input size with scratches')
