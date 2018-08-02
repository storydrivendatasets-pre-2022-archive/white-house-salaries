#!/usr/bin/env bash
for yr in $(seq 2017 2018); do
    pdftotext ./data/raw/${yr}.pdf -layout ./data/raw/poppler/${yr}.txt
done
