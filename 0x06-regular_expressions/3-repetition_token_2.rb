#!/usr/bin/env ruby
# This script will accept one argument and
# pass it to a regular expression matchin method
puts ARGV[0].scan(/hbt{1,4}n/).join
