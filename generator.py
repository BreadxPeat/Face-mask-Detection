train_datagen = ImageDataGenerator(rescale=1./255, zoom_range= 0.2, rotation_range = 40, horizontal_flip= True)

test_datagen= ImageDataGenerator(rescale= 1./255)
validation_datagen= ImageDataGenerator(rescale=1./255)

train_generator= train_datagen.flow_from_directory(train_dir, target_size=(150,150), batch_size= 32, class_mode= 'binary')

test_generator= test_datagen.flow_from_directory(test_dir, target_size=(150,150), batch_size=32, class_mode= 'binary')

valid_generator= validation_datagen.flow_from_directory(valid_dir, target_size=(150,150), batch_size= 32, class_mode= 'binary')

