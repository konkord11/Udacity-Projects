#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#
# PROGRAMMER: Karam Salah Elradie
# DATE CREATED: 15/06/2023
# REVISED DATE:
# PURPOSE: Create a function classify_images that uses the classifier function
#          to create the classifier labels and then compares the classifier
#          labels to the pet image labels. This function inputs:
#            - The Image Folder as image_dir within classify_images and function
#              and as in_arg.dir for function call within main.
#            - The results dictionary as results_dic within classify_images
#              function and results for the function call within main.
#            - The CNN model architecture as model within classify_images function
#              and in_arg.arch for the function call within main.
#           This function uses the extend function to add items to the list
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison
#           of the pet and classifier labels as the item at index 2 of the list.
##

# Imports the classifier function for using CNN to classify images
from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with the classifier function, compares pet labels to
    the classifier labels, and adds the classifier label and the comparison of
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they match the pet image labels.
    The format includes putting the classifier labels in all lowercase
    letters and stripping the leading and trailing whitespace characters from them.
    For example, if the Classifier function returns 'Maltese dog, Maltese terrier, Maltese',
    the classifier label should be 'maltese dog, maltese terrier, maltese'.
    Note that dog names from the classifier function can be a string of dog
    names separated by commas when a particular breed of dog has multiple dog
    names associated with it. For example, you may find pet images of
    a 'dalmatian' (pet label), and it may match the classifier label
    'dalmatian, coach dog, carriage dog' if the classifier function correctly
    classifies the pet images of dalmatians.

    PLEASE NOTE: This function uses the classifier() function defined in
    classifier.py within this function. The proper use of this function is
    in test_classifier.py. Please refer to that program prior to using the
    classifier() function to classify images within this function.

    Parameters:
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string).
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. The list will contain the following items:
                    - index 0: pet image label (string)
                    - index 1: classifier label (string)
                    - index 2: 1/0 (int) where 1 = match between pet image
                                and classifier labels, and 0 = no match between labels.
      model - Indicates which CNN model architecture will be used by the
              classifier function to classify the pet images. The values must
              be either: resnet, alexnet, or vgg (string).
    Returns:
      None - The results_dic dictionary is a mutable data type, so no return is needed.
    """
    for key in results_dic:
        # Call the classifier function to get the classifier label
        classifier_label = classifier(images_dir + key, model)

        # Format the classifier label to match the pet image label format
        classifier_label = classifier_label.lower().strip()

        # Get the pet image label from the results_dic
        pet_label = results_dic[key][0]

        # Check if the pet label and the classifier label both represent dogs or not dogs
        # if ("dog" in pet_label and "dog" in classifier_label) or ("dog" not in pet_label and "dog" not in
        # classifier_label): results_dic[key].extend([classifier_label, 1])

        # Check if the pet label and the classifier label both represent dogs
        if any(breed.strip() == pet_label for breed in classifier_label.split(',')):
            results_dic[key].extend([classifier_label, 1])

        # Otherwise, there is a mismatch between the pet label and the classifier label
        else:
            results_dic[key].extend([classifier_label, 0])
