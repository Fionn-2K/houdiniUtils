#!/bin/bash

for filename in C:/Users/fionn.sherrard/Downloads/assets/obj_test/*.obj; do
  hython script.py "D:/Rebelway/Week_4/Pipeline_template_example.hip" "$filename"
done