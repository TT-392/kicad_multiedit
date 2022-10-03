#!/bin/bash

for f in sources/dark/*; do
    convert -background transparent -resize 20x20 $f $(echo $f | sed 's/sources\(.*\)svg/output\1png/g')
done

for f in sources/light/*; do
    convert -background transparent -resize 20x20 $f $(echo $f | sed 's/sources\(.*\)svg/output\1png/g')
done

