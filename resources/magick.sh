#!/bin/bash

for f in sources/*; do
    convert -background transparent -resize 20x20 $f $(echo $f | sed 's/sources\(.*\)svg/output\1png/g')
done

