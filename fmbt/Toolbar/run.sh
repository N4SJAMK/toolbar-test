mkdir "logs"
fmbt toolbar.conf | tee logs/log$(date +%s).xml
