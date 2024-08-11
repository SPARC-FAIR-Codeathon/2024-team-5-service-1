#!/bin/sh
# set sh strict mode
set -o errexit
set -o nounset
IFS=$(printf '\n\t')

cd /home/scu/file_format_converter

echo "starting service as"
echo   User    : "$(id "$(whoami)")"
echo   Workdir : "$(pwd)"
echo Python Version: "$(python --version)"
echo "..."
echo
# ----------------------------------------------------------------
# This script shall be modified according to the needs in order to run the service
# The inputs defined in ${INPUT_FOLDER}/inputs.json are available as env variables by their key in capital letters
# For example: input_1 -> $INPUT_1

# put the code to execute the service here
# For example:
# env
echo "Input folder content:"
ls -al "${INPUT_FOLDER}"
echo "INPUT_1:", $INPUT_1
echo "INPUT_2:", $INPUT_2
# echo "TEST DATA" > $OUTPUT_FOLDER/outputs_pre.txt

# from the list of files in the input folder, get the first one not named 'inputs.json'
# and use it as the input file
INPUT_FILE=$(ls -1 ${INPUT_FOLDER} | grep -v 'inputs.json' | head -n 1)
echo "INPUT_FILE:", $INPUT_FILE

python main.py $INPUT_FOLDER/$INPUT_FILE $INPUT_2

# then retrieve the output and move it to the $OUTPUT_FOLDER
# as defined in the output labels
# For example: cp output.csv $OUTPUT_FOLDER or to $OUTPUT_FOLDER/outputs.json using jq
echo "Input folder content:"
ls -al "${INPUT_FOLDER}"
echo "Output folder content:"
ls -al "${OUTPUT_FOLDER}"
echo "PWD folder content:"
ls -al

# display the contents of log_output_filepath.txt
echo "Content of log_output_filepath.txt:"
echo "$(cat log_output_filepath.txt)"

cp "$(cat log_output_filepath.txt)" $OUTPUT_FOLDER
# echo "TEST DATA" > $OUTPUT_FOLDER/outputs.txt

#TODO: Replace following
cat > "${OUTPUT_FOLDER}"/outputs.json << EOF
{
    "output_1":"$(cat log_output_filepath.txt)"
}
EOF
