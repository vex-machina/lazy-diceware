BEGIN { print "{"}
{ print "\t" "'" $1 "'" ":", "'" $2 "'" ","}
END { print "}" }
