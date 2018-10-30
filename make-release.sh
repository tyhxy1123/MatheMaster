#!/usr/bin/bash

# MIT License
#
# Copyright (c) 2018 Philipp Joram
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

function msg {
    echo -e "\e[33m::\e[0m" $@ 1>&2
}

trap \
    "{ msg 'an error occured!'; exit 1; }" \
    SIGINT SIGTERM ERR

function mkversion {
    local date=$(date +%Y%m%d)
    local rev_list_args=$(git rev-parse --after=yesterday)
    local commits_today=$(git rev-list --count $rev_list_args HEAD)
    echo $date-$commits_today
}

VERSION=$(mkversion)
WORK_DIR=$(mktemp -d)

OUT_DIR="release-$VERSION"
msg "creating output directory $OUT_DIR..."

if [[ -e $OUT_DIR ]]
then
    msg "output directory already exists, refusing to overwrite files"
    exit 1
fi
mkdir $OUT_DIR

# compile a .pdf file for each lecture
for lecture in MFANA MSTAT ORDSTR PDENUM WTHM FEM ANGA AMGEO
do
    pushd $lecture
    msg "compiling lecture $lecture..."
    latexmk \
        -pdf \
        -output-directory="$WORK_DIR" \
        -quiet \
        -halt-on-error
    popd
done

msg "copying final .pdf files to output directory..."
cp $WORK_DIR/*.pdf $OUT_DIR

msg "creating release tarball..."
TARBALL="$OUT_DIR.tar.gz"
tar -cvzf $TARBALL $OUT_DIR
mv $TARBALL $OUT_DIR

msg "cleaning up..."
rm -r $WORK_DIR

msg "DONE! Files written to $OUT_DIR and ready for distribution!"
