# These are the jsons ordered by threshold ....

files=(jsons_2023/current/L1_*_HLT_*_Incl_Final.json)
files=(`printf '%s\n' "${files[@]}"|sort -V`)

for i in ${!files[@]}; do
    #echo $i,${files[$i]}
    FILE_TOTAL=${files[$i]//'Incl_Final.json'/}'Excl_Final.json'
    # cp ${files[$i]} $FILE_TOTAL
    if [[ $i -gt 0 ]]; then
	echo "index: $i, file[i]: ${files[$i]}, file[i-1]: ${files[$i-1]}"
	# eval 'compareJSON.py --or ${files[$i]} ${files[$i-1]}'
	# echo "$FILE_TOTAL" 
	eval 'compareJSON.py --sub ${files[$i]} ${files[$i-1]} ${files[$i]}_total'
    else
	echo "index: $i, file[i]: ${files[$i]}"
    fi
done
