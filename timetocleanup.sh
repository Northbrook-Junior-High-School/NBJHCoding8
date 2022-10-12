now=$(date +"%T")
day='date +%u'

weekday=0
echo "Current Time: $now"

while :
do
  now=$(date +"%T")
  if [ "${now}" == '11:05:00' ]
  then
    afplay timetocleanup.mp3

  elif [ "${now}" == '9:59:00' ]
  then
    afplay timetocleanup.mp3

  elif [ "${now}" == '10:42:00' ]
  then
    afplay timetocleanup.mp3

  elif [ "${now}" == '11:25:00' ]
  then
    afplay timetocleanup.mp3

  elif [ "${now}" == '2:50:00' ]
  then
    afplay timetocleanup.mp3

  elif [ "${now}" == '3:33:00' ]
  then
    afplay timetocleanup.mp3
  fi
done