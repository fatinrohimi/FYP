. $(atf_get_srcdir)/utils.subr

atf_test_case "v4" "cleanup"
v4_head()
{
  atf_set descr 'Basic pass/block test for IPv4'
  atf_set require.user root
 }
 
 v4_body()
 {
    pft_init 
    
    epair=$(pft_mkepair)
    ifconfig ${epair}a 192.0.2.1/24 up
    
    #set up a simple jail with one interface
    pft_mkjail alcatraz ${epair}b
    jexec alcatraz ifconfig ${epair}b 192.0.2.2/24 up
    
    #trivial ping to the jail,without pf
    atf_check -s exit:0 -o ignore ping -c 1 -t 1 192.0.2.2
    
    #pf without policy will lwt us ping
    jexec alcatraz pfctl -e
    atf_check -s exit:0 -o ignore ping -c 1 -t 1 192.0.2.2
    
    #block everything
    pft_set_rules alcatraz "block in"
    atf_check -s exit:2 -o ignore ping -c 1 -t 1 192.0.2.2
    
    v4_cleanup()
    {
        pft_cleanup
     }
     
     atf_init_test_cases()
     {
        atf_add_test_case "v4"
      }
