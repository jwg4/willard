print """$t=$s=q($t =~ s/\\\\/\\\\\\\\/g; print 'print \"\"\"$t=$s' . "=q($t);\\n$s\\n";);
$t =~ s/\\\\/\\\\\\\\\\\\\\\\/g; print 'print \"\"\"$t=$s' . "=q($t);\\n$s\\n";"""
