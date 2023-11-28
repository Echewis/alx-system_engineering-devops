#!/usr/bin/env ruby
# This ruby script will accept one argument and
# pass it to a regular expression matching method
puts ARGV[0].scan(/(?!hbon\b)\b\w+/).join
