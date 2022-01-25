function getCookie(cname)
{
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for (var i = 0; i < ca.length; i++)
  {
    var c = ca[i];
    while (c.charAt(0) == ' ')
    {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0)
    {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function setCookie(cname, cvalue, exdays)
{
  var d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  var expires = "expires=" + d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

var delete_cookie = function(name)
{
  document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
  document.cookie = 'account_name=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
  window.location = '/login';
};

function get_jwt_token()
{
  var api_key = getCookie("RuleEngine");
  return api_key;
}

function get_promote_token()
{
  var api_key = getCookie("promote_token");
  return api_key;
  // return get_jwt_token();
}

function get_account_id()
{
  var account_id = parseInt(getCookie("account_details").split(',')[1]);
  return account_id;
}

function get_user_role(){
  var role = parseInt(getCookie("user_role"));
  return role;
}

function get_promote_account_id()
{
  var account_id = parseInt(getCookie("promote_account_id"));
  return account_id;
}

function get_account_name()
{
  var account_name = getCookie("account_details").split(',')[0];
  return account_name;
}

function update_ruleset_properties(response)
{
  html = `<table class="table table-bordered table-hover">
            <tr>
                <td><b> Listening : </b><input id=event_payload_state type="checkbox" class="BSswitch" data-on-text='Disable' data-off-text='Enable' name="my-checkbox"></td>
            </tr>
            <tr>
                <td><b> EventPayload ID :</b> ${response['event_payload_id']}
                <input type=hidden id=event_payload_id value=${response['event_payload_id']}></td>
            </tr>
            <tr>
                <td><b> Ruleset ID :</b> ${response['ruleset_id']} </td>
            </tr>
            <tr>
                <td><b> Major version : </b> ${response['major_version']}</td>
            </tr>
            <tr>
                <td><b> Minor version : </b> ${response['minor_version']}</td>
            </tr>
            <tr>
                <td><b> Module :</b> ${response['module']}</td>
            </tr>
            <tr>
                <td><b> account ID :</b> ${response['account_id']} </td>
            </tr>
            <tr>
                <td><b> Ruleset created_at :</b> ${response['ruleset_created_at']} </td>
            </tr>
            <tr>
                <td><b> Ruleset updated_at :</b> ${response['ruleset_updated_at']} </td>
            </tr>
            <tr>
                <td><b> EventPayload created_at :</b> ${response['event_payload_created_at']} </td>
            </tr>
            <tr>
                <td><b> EventPayload updated_at :</b> ${response['event_payload_updated_at']} </td>
            </tr>
            </table>`
  document.getElementById('ruleset_properties').innerHTML = html;
}


function update_state(element, event, state, event_payload_id)
{
  $.ajax({
    'url': '/api/v1/state/' + event_payload_id,
    'type': 'PUT',
    beforeSend: function(xhr) {
      xhr.setRequestHeader('Authorization', get_jwt_token());
    },
    data: {
      "account_id": get_account_id(),
      "state": state
    },
    success: function(response) {
      notify('top-right', 'EventPayload updated successfully');
    },
    error: function(error) {
      notify('top-right', 'Eventpayload update failed', 'danger');
    }
  })
}

function load_rule_set(event_payload_id)
{
  var message_editor = ace.edit("rule_set_area");
  $.ajax({
    url: '/api/v1/ruleset/' + event_payload_id,
    type: 'GET',
    data: {
      "account_id": get_account_id()
    },
    beforeSend: function(xhr) {
      xhr.setRequestHeader('Authorization', get_jwt_token());
    },
    success: function(response) {
      message_editor.session.setValue(response['ruleset']);
      $('#ruleset_title').html(`
        <h4 style='display:inline;'>${response['payload_type']}</h4>
        <a style='float:right;cursor:pointer;' onclick="showHistory('rulesets',${response['ruleset_id']})">View History</a>
        `);
      if(response['promoted_to_all_pods'] == false || user_role == 0){
        message_editor.setReadOnly(true);
        $('#ruleset_update_btn').prop("disabled", true);
      }else{
        message_editor.setReadOnly(false);
        $('#ruleset_update_btn').prop("disabled", false);
      }
      if(response['promoted_to_all_pods'] == false){
        notify('top-right', 'You cannot modify this ruleset because another person is working on this');
      }
      update_ruleset_properties(response);
      $(".BSswitch").bootstrapSwitch();
      if (response["listening"] == 1) {
        $(".BSswitch").bootstrapSwitch('state', true);
      }
      if(user_role != 0){
        $(".BSswitch").on('switchChange.bootstrapSwitch', function(event, state) {
          update_state(this, event, state, $('#event_payload_id').val())
        });
      }else{
        $(".BSswitch").bootstrapSwitch('disabled',true);
      }
    },
    error: function(error) {
      alert(error);
    }
  })
}

function load_rule(rule_id)
{
  $.ajax({
    'url': '/api/v1/rule/' + rule_id,
    'type': 'GET',
    data: {
      "account_id": get_account_id()
    },
    beforeSend: function(xhr) {
      xhr.setRequestHeader('Authorization', get_jwt_token());
    },
    success: function(response) {
      $('#rule_title').html(`
        <h4 style='display:inline;'> ${response['data']['name']}- v${response['data']['version']}</h4>
        <a style='float:right;cursor:pointer;' onclick="showHistory('rules',${rule_id})">View History</a>
        `);
      var target_schema = ace.edit("target_schema");
      var rules_editor = ace.edit("rules_editor");
      target_schema.setValue(response['data']['target_schema']);
      rules_editor.setValue(response['data']['rules']);
      if(response['data']['promoted_to_all_pods'] == false || user_role == 0 ){
        target_schema.setReadOnly(true);
        rules_editor.setReadOnly(true);
        $('#rules_update_btn').prop("disabled", true);
      }else{
        target_schema.setReadOnly(false);
        rules_editor.setReadOnly(false);
        $('#rules_update_btn').prop("disabled", false);
      }
      if(response['data']['promoted_to_all_pods'] == false){
        notify('top-right', 'You cannot modify this rule because another person is working on this');
      }
      $('#rule_id').val(rule_id);
    },
    error: function(error) {
      console.log(error);
      alert(error)
    }
  })
}

function load_udf(udf_id) {
  $.ajax({
    'url': 'api/v1/udf/' + udf_id,
    'type': 'GET',
    data: {
      "account_id": get_account_id()
    },
    beforeSend: function(xhr) {
      xhr.setRequestHeader('Authorization', get_jwt_token());
    },
    success: function(response) {
      $('#method_title').html("<h4>" + response['data']['name'] + "</h4>");
      var udf_editor = ace.edit("udf_editor",{
                      mode: "ace/mode/python",
                      selectionStyle: "text"});
      console.log(response['data'])
      udf_editor.setValue(response['data']['definition']);

      $('#udf_id').val(udf_id);
    },
    error: function(error) {
      console.log(error);
    }
  })
  $("#udfModalLabel").html("Update Method")
  $("#model_udf_button").attr("onclick", "update_udf_definition()");
  $("#model_udf_button").text("Update");
  $("#udf_model").modal();
  checkRoleAndRemoveButton('#model_udf_button', user_role)
}

function load_service(service_id) {
  Clear()
  $.ajax({
    'url': '/api/v1/service/' + service_id,
    'type': 'GET',
    data :{
      "account_id": get_account_id()
    },
    beforeSend: function(xhr) {
      xhr.setRequestHeader('Authorization', get_jwt_token());
    },
    success: function(response) {
      $("#service_name").val(response["data"]["name"]);
      $("#retry_count").val(
        response["data"]["transformation_retry_count"]);
      $('#reports_config').val(response["data"]["reports_config"]);
      $('#api_push_retry_count').val(
        response["data"]["api_push_retry_count"]);
      $('#service_id').val(service_id);
      $('#toggle-button').val(response["data"]["state"]);
      $('#webhook_url').val(response["data"]["webhook_url"]);
      var temp = 2;
      for (x in response["data"]["transformation_success_topic"])
      {
        if (x == 0)
        {
          $('#success_topic').val(response["data"]["transformation_success_topic"][x]);
          $('#payload_type').val(response["data"]["payload_type"][x]);
        } else
        {
          Add_Field();
          $('.removeclass' + field + ' #success_topic').val(response["data"]["transformation_success_topic"][x]);
          $('.removeclass' + field + ' #payload_type').val(response["data"]["payload_type"][x]);
        }
      }
    },
    error: function(error) {
      console.log(error);
      alert(error);
    }
  })
  $("#serviceModalLabel").html("Update Service")
  $("#service_modal_button").attr("onclick", "update_service()");
  $("#service_modal_button").text("Update");
  $("#service_Modal").modal();
  checkRoleAndRemoveButton('#service_modal_button', user_role);
}

function load_permanent_failed_message(s3_message_key)
{
  $("#load_icon").show()
  $.ajax({
    url: '/api/v1/permanent_failed_message',
    type: 'GET',
    data: {
          "account_id": get_account_id(),
          "key": s3_message_key
    },
    beforeSend: function(xhr) {
      xhr.setRequestHeader('Authorization', get_jwt_token());
    },
    success: function(response) {
      $("#load_icon").hide()
      var message_editor = ace.edit("message_editor");
      message_editor.setValue(JSON.stringify(response["data"], undefined, 2));
      $("#message_view_modal").modal();
      checkRoleAndRemoveButton('#permanent_failed_retry_btn', user_role)
    },
    error: function(error) {
      $("#load_icon").hide()
      console.log(error);
    }
  })
}

var user_role = get_user_role();
var disabled_payloads_table = undefined;
$(document).ready(function()
{
  if(window.location.pathname.split('/')[1] != 'login' && getCookie("created_time") == "") {
     delete_cookie('RuleEngine')
     delete_cookie('user_role')
     delete_cookie('created_time')
  }
  $("#account_id").val(get_account_id());
  api_key = get_jwt_token();
  account_id = get_account_id();
  var ele = $("#switch_account").val(account_id);
  console.log(ele)
  $("#switch_account").change()

  if(window.location.href.indexOf("/home") > -1){
    $.ajax({
      'url': `/api/v1/event_payloads`,
      'type': 'GET',
      'async' : false,
      'data': {
        'account_id': get_account_id()
      },
      'headers':{
        'Authorization' : get_jwt_token()
      },
      success: function(response){

        disabled_payloads = [];
        var index = 0;
        response.data.forEach(function (item) {
          if(item.state == false){
            var obj = {};
            obj['s_no'] = index + 1;
            obj['name'] = item.payload_type + ' -v' + item.major_version + '.' + item.major_version
            obj['status'] = `<button class="btn btn-small btn btn-danger" type="button">Disabled</button>`
            disabled_payloads.push(obj);
            index = index + 1;
          }
        });

        if(disabled_payloads.length > 0){
          if(disabled_payloads_table != undefined) {
            disabled_payloads_table.destroy();
          }

          disabled_payloads_table = $('#disabled_payloads_table').DataTable({
              data: disabled_payloads,
              "columns": [{'data': 's_no'}, {'data': 'name'}, {'data':  'status'}],
              aoColumnDefs: [
              {
                bSortable: false,
                aTargets: [ 0 ]
              }]
          });
        }
      },
      error: function(local_error){
        showErrorAlert(local_error)
      }
    });
  }

  var Eventpayloads_table = $('#Eventpayloads').DataTable(
    {
      "ajax": {
        url: '/api/v1/event_payloads',
        type: "GET",
        data: {
          'account_id': get_account_id()
        },
        beforeSend: function(request) {
          request.setRequestHeader("Authorization", api_key);
        }
      },
      "columns": [
        {
          "data": null,
          render: function(data, type, row, meta) {
            return data['payload_type'] + '- v' + data['major_version'] + "." + data['minor_version'];
        }
      }]
  });

  checkRoleAndRemoveButton('#rules_create_btn', user_role)
  checkRoleAndRemoveButton('#rules_update_btn', user_role)
  checkRoleAndRemoveButton('#ruleset_create_btn', user_role)
  checkRoleAndRemoveButton('#ruleset_update_btn', user_role)
  checkRoleAndRemoveButton('#promote_tab', user_role)
  checkRoleAndRemoveButton('#import_tab', user_role)

  var services_table = $('#services_table').DataTable(
    {
      dom: 'l<"dom_element">frtip',
      initComplete: function() {
        if(user_role != 0){
          $("div.dom_element").html(
            '&nbsp <button onclick="Clear()""  \
                    role="button" data-toggle="modal" class="btn btn-primary"> \
                      Create \
                      </button>');
        }
      },
      "ajax": {
        url: '/api/v1/services',
        type: "GET",
        data: {
          'account_id': get_account_id()
        },
        beforeSend: function(request) {
          request.setRequestHeader("Authorization", api_key);

        }
      },
      "columns": [
        {
          "data": null,
          render: function(data, type, row, meta) {
            return data['name'];
          }
        },
        {
          "data": null,
          render: function(data, type, row, meta) {
            return data['retry_count'];
          }
        },
        {
          "data": null,
          render: function(data, type, row, meta) {
            return data['api_push_retry_count'];
          }
        },
        {
          "data": null,
          render: function(data, type, row, meta) {
            return data['created_at'];
          }
        },
        {
          "data": null,
          render: function(data, type, row, meta) {
            return data['updated_at'];
          }
        },
        {
          'target': 0,
          'searchable': false,
          'orderable': false,
          'className': 'dt-body-left',
          "data": null,
          render: function(data, type, full, meta) {
            return '<input id="toggle-button" disabled="true" type="checkbox" checked data-toggle="none" data-on="Enabled" data-off="Disabled" data-onstyle="success" data-offstyle="danger">';
          }
        },
      ],
      "fnDrawCallback": function() {
        jQuery('#services_table #toggle-button').bootstrapToggle();
      }

  });

  var rules_table = $('#rules_table').DataTable(
    {
    "ajax": {
        url: 'api/v1/rules',
        type: "GET",
        data: {
            'account_id': get_account_id()
        },
        beforeSend: function(request) {
          request.setRequestHeader("Authorization", api_key);
        }
      },
      "columns": [
        {
          "data": null,
          render: function(data, type, row, meta) {
            return data['name'] + '- v' + data['version'];
          }
        }]
  });

var permanent_failed_messages_table = $('#permanent_failed_messages_table').DataTable(
    {
      "ajax": {
        url: '/api/v1/permanent_failed_messages',
        type: "GET",
        data: {
            'account_id': get_account_id()
        },
        beforeSend: function(request) {
          request.setRequestHeader("Authorization", api_key);
        }
      },

      "columns": [
        {
          'target': 0,
          'searchable': false,
          'orderable': false,
          'className': 'dt-body-left',
          "data": null,
          render: function(data, type, full, meta) {
            return ' <input type = "checkbox" name = "id[]" value = "' +
              $('<div/>').text(data['key']).html() + '">';
          }
        },
        {
          "targets": 1,
          "visible": false,
          "searchable": false,
          "data": null,
          render: function(data, type, full, meta) {
            return data['key'];
          }
        },

        {
          "data": null,
          render: function(data, type, row, meta) {
            return data['uuid'];
          }
        },
        {
          "data": null,
          render: function(data, type, row, meta) {
            return data['service'];
          }
        },

        {
          "data": null,
          render: function(data, type, row, meta) {
            return data['payload_type'];
          }
        },
        {
          "data": null,
          render: function(data, type, row, meta) {
            return data['last_modified'];
          }
        },
        {
          'target': 0,
          'searchable': false,
          'orderable': false,
          'className': 'dt-body-left',
          "data": null,
          render: function(data, type, full, meta) {
            return '<a href="#" id="delete"> \
                    <img src="/static/trash.png" style="width:20px;height:20px;"> \
                  </a>';
          }
        },



      ],
      'order': [1, 'asc'],
      dom: 'lfrtp<"retry_button">',
      initComplete: function() {
        if(user_role != 0){
          $("div.retry_button").html(
          '&nbsp <br><input type="submit" class="btn btn-primary pull-left" id="retry_button"  \
                      value =Retry >');
        }
      },
  })

  $('#select-all').on('click', function() {
    var rows = permanent_failed_messages_table.rows(
      {
        'search': 'applied'
      }).nodes();
    $('input[type="checkbox"]', rows).prop('checked', this.checked);
  });

  $('#permanent_failed_messages_table tbody').on('change', 'input[type="checkbox"]', function() {
    if (!this.checked)
    {
        var el = $('#select-all').get(0);
        if (el && el.checked && ('indeterminate' in el))
        {
          el.indeterminate = true;
        }
    }
  });


  $('#datatable_form').on('submit', function(e) {
    var form = this;
    var keys = [];
    permanent_failed_messages_table.$('input[type="checkbox"]').each(function() {
      if (this.checked)
      {
        keys.push(this.value)
      }
    });
    $.ajax({
      url: '/api/v1/permanent_failed_messages',
      type: 'POST',
      data: {
            'Keys': keys,
            'account_id': get_account_id()
      },
      beforeSend: function(request) {
        request.setRequestHeader("Authorization", api_key);
      },
      error: function(error_message) {
        if (error_message.responseJSON['message'])
        {
          notify('top-right', 'Failed to publish\n message : ' + error_message.responseJSON['message'], 'danger');
          setTimeout(document.location.reload(), 2000);

        }
        else
          notify('top-right', 'Failed to publish', 'danger');
          setTimeout(document.location.reload(), 2000);
      },
      success: function(response) {
        notify('top-right', 'successfully published to failed_topic');
        setTimeout(document.location.reload(), 2000);
      },
    })

  })

  $('#search_form').on('submit', function(e) {
    // $("#permanent_failed_messages_table").dataTable().fnClearTable()
    $("#load_icon").show()
    var service = $("#service").val()
    var payload_type = $("#payload_type").val()
    $.ajax({
      url: '/api/v1/permanent_failed_messages',
      type: 'GET',
      dataType: 'json',
      data: {
            'account_id': get_account_id(),
            'service': service,
            'payload_type': payload_type,
      },
      beforeSend: function(xhr) {
        xhr.setRequestHeader('Authorization', get_jwt_token());
      },
      success: function(response) {
        $("#load_icon").hide()
        data = response['data'];
        $("#permanent_failed_messages_table").dataTable().fnClearTable()
        permanent_failed_messages_table.rows.add(data).draw();
      },
      error: function(error) {
        $("#load_icon").hide()
        if (error.responseJSON['message']) {
          notify('top-right', "something went wrong");
        }

      }
    })

  })

  var udf_table = $("#udf_table").DataTable({
    dom: '<"dom_element">frtip',
    "pageLength": 5,
    initComplete: function() {
      if(user_role !=0){
        $("div.dom_element").html(
          '&nbsp <button id="udf_create_btn" onclick="clear_udf()""  \
                  role="button" data-toggle="modal" class="btn btn-primary"> \
                    Create \
                    </button>');
      }
    },
    "ajax": {
      "url": 'api/v1/udfs',
      "type": "GET",
      data: {
        'account_id': get_account_id()
      },
      "beforeSend": function(request) {
        request.setRequestHeader("Authorization", api_key);
      }
    },
    "columns": [{
      "data": null,
      render: function(data, type, row, meta) {
        return data['id'];
      }
    },
    {
      "data": null,
      render: function(data, type, row, meta) {
        return data['name'];
      }
    },
    {
      "data": null,
      render: function(data, type, row, meta) {
        return data['arguments'];
      }
    },
    {
      "data": null,
      render: function(data, type, row, meta) {
      if(data['status'] == 1)
        return '<p style="color:green">approved</p>'
      else if(data['status'] == 0){
        return '<p style="color:blue">pending</p>'
      }
      else{
        return '<p style="color:red">Rejected</p>'
      }
    }
  },
  {
    "data": null,
    render: function(data, type, row, meta) {
      return data['updated_at'];
    }
  },
  {
    'target': 0,
    'searchable': false,
    'orderable': false,
    'className': 'dt-body-center',
    "data": null,
    render: function(data, type, full, meta) {
      if(data['role'] == 2){
          return data['udf_accept']

        }else{
          udf_table.columns([5]).visible(false)
          return ''
        }
    }

  },
  {
    'target': 0,
    'searchable': false,
    'orderable': false,
    'className': 'dt-body-center',
    "data": null,
    render: function(data, type, full, meta) {
      if(data['role'] == 2){
          return data['udf_reject']

        }else{
          udf_table.columns([6]).visible(false)
          return ''
        }
    }

  },
  {
    'target': 0,
    'searchable': false,
    'orderable': false,
    'className': 'dt-body-center',
    "data": null,
    render: function(data, type, full, meta) {
      if(data['role'] == 2){
          return data['udf_trash']

        }else{
          udf_table.columns([7]).visible(false)
          return ''
        }
    }
  },
  {
    'target': 0,
    'searchable': false,
    'orderable': false,
    'className': 'dt-body-center',
    "data": null,
    render: function(data, type, full, meta) {
      return `<a onclick="showHistory('udfs',${data['id']})"><button class="btn btn-small btn btn-success" type="button">History</button></a>`
    }
  }
  ]
  })

  $('#udf_table tbody').on('click', 'td:nth-last-child(0)', function() {
    if ($(this).hasClass('selected'))
    {
      $(this).removeClass('selected');
    }
    else
    {
      udf_table.$('tr.selected').removeClass('selected');
      $(this).addClass('selected');
    }
    var data = udf_table.row(this).data();
    if(data['status'] == 1)
      return false
    var retVal = confirm("Do you want to delete method ?");

    if (retVal==true) {
       $.ajax ({
         "url": '/api/v1/udf/'+data['id'],
         "type": "DELETE",
         "data": {
           "id": data['id'],
           "account_id": get_account_id(),
           "name": data['name']
         },
         "beforeSend": function(request) {
           request.setRequestHeader("Authorization", api_key);
         },
         success: function(response) {
           notify('top-right', "Successfully deleted")
           setTimeout(document.location.reload(), 20000);

         },
         error: function(error) {
           if (error.responseJSON['message']){
              notify('top-right', error.responseJSON['message'])
            }
            else {
              notify('top-right',"something went wrong")
            }
            setTimeout(document.location.reload(), 20000);

         }
       });
   }

  });

  $('#udf_table tbody').on('click', 'td:nth-last-child(4)', function() {
    if ($(this).hasClass('selected'))
    {
      $(this).removeClass('selected');
    }
    else
    {
      udf_table.$('tr.selected').removeClass('selected');
      $(this).addClass('selected');
    }
    var data = udf_table.row(this).data();
    if(data['status'] == 1 || data['status'] == -1)
      return false
     update_udf_state(id = data['id'],name = data['name'],status = 1)
  });

  $('#udf_table tbody').on('click', 'td:nth-last-child(3)', function() {
    if ($(this).hasClass('selected'))
    {
      $(this).removeClass('selected');
    }
    else
    {
      udf_table.$('tr.selected').removeClass('selected');
      $(this).addClass('selected');
    }
    var data = udf_table.row(this).data();
    if(data['status'] == 1 || data['status'] == -1)
      return false
     update_udf_state(id = data['id'],name = data['name'],status = -1)
  });

  var users_table = $('#users_table').DataTable({
    dom: 'l<"dom_element">frtip',
    initComplete: function() {
      if(user_role !=0){
        $("div.dom_element").html(
          '&nbsp <button type="button" id="add_user" href="#add_user_modal"  \
            role="button" data-toggle="modal" class="btn btn-primary"> \
              Add_User \
            </button>');
      }
    },
    "ajax": {
      "url": '/api/v1/users',
      "type": "GET",
      data: {
            'account_id': get_account_id()
      },
      beforeSend: function(request) {
        request.setRequestHeader("Authorization", api_key);
      }
    },
    failed: function(jqXHR, textStatus, errorThrown) {
      alert(textStatus);
    },
    "columns": [
      {
        "data": null,
        "visible": false,
        render: function(data,type,row,meta) {
          return data['id'];
        }
      },
      {
        "data": null,
        render: function(data, type, row, meta) {
          return data['name'];
        }
      },
      {
        "data": null,
        render: function(data, type, row, meta) {
          return data['email'];
        }
      },
      {
        "data": null,
        render: function(data, type, row, meta) {
          if (data['role'] == 2){
            return 'Super Admin';
          }
          else if(data['role'] == 1){
            return 'Admin'
          }
          else{
            return 'Read Only'
          }
        }
      },
      {
        'target': 0,
        'searchable': false,
        'orderable': false,
        'className': 'dt-body-left',
        "data": null,
        render: function(data, type, full, meta) {
          if(user_role != 0 ){
            return '<a href="#" id="remove_user"> \
              <img src="/static/trash.png" style="width:20px;height:20px;"> \
            </a>';
          }else{
            return '';
          }

        }
      },
    ],

  });

  var topics_table = $('#topics_table').DataTable({
    dom: 'l<"dom_element">frtip',
    initComplete: function() {
      $("div.dom_element").html(
        `&nbsp <button type="button" id="add_topics" href="#add_topics_modal" \
          role="button" data-toggle="modal" class="btn btn-primary"> \
            Configure Topics \
          </button>`);
    },
    "ajax": {
      "url": '/api/v1/topics',
      "type": "GET",
      data: {
            'account_id': get_account_id()
      },
      beforeSend: function(request) {
        request.setRequestHeader("Authorization", api_key);
      }
    },
    failed: function(jqXHR, textStatus, errorThrown) {
      alert(textStatus);
    },
    "columns": [
      {
        "data": null,
        "visible": false,
        render: function(data,type,row,meta) {
          return data['id'];
        }
      },
      {
        "data": null,
        render: function(data, type, row, meta) {
          return data['name'];
        }
      },
      {
        "data": null,
        render: function(data, type, row, meta) {
          return data['partitions'];
        }
      },
      {
        "data": null,
        render: function(data, type, row, meta) {
          return data['rpm'];
        }
      },
      {
        "data": null,
        render: function(data, type, row, meta) {
          return data['transformation_group_id'];
        }
      },
      {
        "data": null,
        render: function(data, type, row, meta) {
          return data['push_group_id'];
        }
      },
      {
        "data": null,
        render: function(data, type, row, meta) {
          return data['configured_at'];
        }
      },
      {
        "data": null,
        render: function(data, type, row, meta) {
          status = data['status']
          if(status == 1){
            return `<button class="btn btn-small btn btn-success" type="button">Active</button>`
          }else if(status == 0){
            return `<button class="btn btn-small btn btn-danger" type="button">Pending</button>`
          }
        }
      }
    ]

  });

  $('#services_table tbody').on('click', 'td:last-child', function() {
    id = services_table.row($(this).closest("tr")).data().id;

    if (services_table.row(this).data().state == 0)
    {
      state = 1;
      services_table.row(this).data().state = 1;
    }
    else
    {
      state = 0;
      services_table.row(this).data().state = 0;
    }
  });



  $('#Eventpayloads tbody').on('click', 'tr', function() {
    if ($(this).hasClass('selected'))
    {
      $(this).removeClass('selected');
    }
    else
    {
      Eventpayloads_table.$('tr.selected').removeClass('selected');
      $(this).addClass('selected');
    }
    var data = Eventpayloads_table.row(this).data();
    load_rule_set(data['id']);
  });

  $('#permanent_failed_messages_table tbody').on('click', 'td:not(:first-child,:last-child)','tr', function() {
    if ($(this).hasClass('selected'))
    {
      $(this).removeClass('selected');
    }
    else
    {
      permanent_failed_messages_table.$('tr.selected').removeClass('selected');
      $(this).addClass('selected');
    }
    var data = permanent_failed_messages_table.row(this).data();
    load_permanent_failed_message(data['key']);
  })

  $('#users_table tbody').on('click', 'td:last-child', function() {
      if ($(this).hasClass('selected')) {
        $(this).removeClass('selected');
      } else {
        users_table.$('tr.selected').removeClass('selected');
        $(this).addClass('selected');
      }
      var data = users_table.row(this).data();
      user_id = data["id"]
      if(user_role !=0 ){
        var retVal = confirm("Do you want to delete user ?");
        if (retVal == true) {
          $.ajax({
            'url': '/api/v1/user/'+user_id,
            'type': 'DELETE',
            'data':{
              "email": data["email"],
              "name": data["name"],
              "role": data["role"],
              "account_id": get_account_id()
            },
            "beforeSend": function(request) {
              request.setRequestHeader("Authorization", api_key);
              // request.setRequestHeader('account_id',account_id);
            },
            success: function(response) {
              notify('top-right', 'User removed successfully');
              console.log(response['signout'])
              // location.reload(true)
              if (response['signout'] == 1)
              {
                signOut()
              }
              else{
                  setTimeout(document.location.reload(), 20000);
              }
            },
            error: function(error_message) {
              if (error_message.responseJSON['message']) {
                notify('top-right', 'Remove user fialed \n message : ' + error_message.responseJSON['message'], 'danger');

            }
            else
              notify('top-right', 'Remove user failed', 'danger');
          }
        });
        }
      }
  });

  $('#permanent_failed_messages_table tbody').on('click', 'td:last-child', function() {
    console.log($(this))
    if ($(this).hasClass('selected'))
    {
      $(this).removeClass('selected');
    }
    else
    {
      permanent_failed_messages_table.$('tr.selected').removeClass('selected');
      $(this).addClass('selected');
    }
    var data = permanent_failed_messages_table.row(this).data();
    console.log(data)
    var retVal = confirm("Do you want to delete message ?");
    if (retVal == true)
    {
      $.ajax({
        'url': 'api/v1/permanent_failed_messages',
        'type': 'DELETE',
        'data': {
          "key": data['key'],
          "account_id": get_account_id()
        },
        "beforeSend": function(request) {
          request.setRequestHeader("Authorization", api_key);
        },
        success: function(response) {
          notify('top-right', 'Message deleted successfully');
          setTimeout(document.location.reload(), 20000);
        },
        error: function(error_message) {
          if (error_message.responseJSON['message'])
          {
            notify('top-right',  'Fialed to delete message \n message : ' + error_message.responseJSON['message'], 'danger');

          }
          else
            notify('top-right', 'Failed to delete message', 'danger');
        }
      });
    }
  });


  $('#rules_table tbody').on('click', 'tr', function() {
    if ($(this).hasClass('selected'))
    {
      $(this).removeClass('selected');
    }
    else
    {
      rules_table.$('tr.selected').removeClass('selected');
      $(this).addClass('selected');
    }
    var data = rules_table.row(this).data();
    load_rule(data['id']);
  });

  $('#udf_table tbody').on('click', 'td:not(:nth-last-child(4), :nth-last-child(3), :nth-last-child(2), :nth-last-child(1))','tr', function() {
    if ($(this).hasClass('selected'))
    {
      $(this).removeClass('selected');
    }
    else
    {
      udf_table.$('tr.selected').removeClass('selected');
      $(this).addClass('selected');
    }
    var data = udf_table.row(this).data();
    load_udf(data['id']);
    $("#udf_model").modal()
  })

  $('#services_table tbody').on('click', 'td:not(:last-child)','tr', function() {
    if ($(this).hasClass('selected')) {
      $(this).removeClass('selected');
    }
    else
    {
      services_table.$('tr.selected').removeClass('selected');
      $(this).addClass('selected');
    }
    var data = services_table.row(this).data();
    load_service(data['id']);
  });


  if ($('#service').length) {
    $.ajax({
      url: '/api/v1/services',
      type: 'GET',
      async: false,
      data: {
            'account_id': get_account_id(),
      },
      beforeSend: function(request) {
        request.setRequestHeader("Authorization", api_key);
      },
      success: function(response) {
        services = response["data"]
        $('.form-inline .services').typeahead({
          source: function(query, process) {
            objects = [];
            map = {};
            $.each(services, function(i, object) {
              map[object] = object['name'];
              objects.push(object['name'])
            });
            process(objects);

          },
          updater: function(item) {
            $('#service_id').val(item);
            return item;
          },
          minLength: 1
        });
      }
    })
  }



  if ($("#switch_account").length) {
    var accounts
    $.ajax({
      url: '/api/v1/accounts',
      type: 'GET',
      data: {
            'account_id': get_account_id()
      },
      dataType: 'json',
      beforeSend: function(request) {
        request.setRequestHeader('Authorization', get_jwt_token());
      },
      success: function(response) {
        accounts = response["accounts"];
        output = [];
        $.each(accounts, function(key, value) {
          var select = document.getElementById('switch_account');
          var opt = document.createElement('option');
          opt.value = value.account_id;
          opt.innerHTML = value.account_name;
          select.appendChild(opt);
        });
        $('.selectpicker').selectpicker('val', get_account_id);
        $('.selectpicker').selectpicker('refresh');
      },
      error: function(error) {
        console.log(error);
      }
    })
  }

  $('select.selectpicker').on('change', function(evt, item)
  {
    account_id = $(this).children("option:selected").val();
    account_name = $(this).children("option:selected").text();
    setCookie("account_details", [account_name, account_id], 6);
    location.reload(true);

  })

});


function onSignIn(googleUser) {
var profile = googleUser.getBasicProfile();
var email = (profile.getEmail()); // This is null if the 'email' scope is not present.
console.log(email)
var token = googleUser.getAuthResponse().id_token;
$.ajax({
  'url': '/api/v1/signin',
  'type': 'POST',
  'data': {
    'account_id': account_id,
    'token' : token,
    'login_type': 'oauth'
  },
  success: function(response){
    setCookie("RuleEngine", response['auth-token'], 6)
    setCookie("account_details", [response['account_name'],response['account_id']], 6)
    setCookie("email", email, 6)
    setCookie("name", response['name'], 6)
    setCookie("user_role", response['role'], 6)
    setCookie("created_time", new Date())
    window.location = '/home';
  },
  error: function(error){
    alert('Authentication failed');
    signOut()
  }
})
}

function signOut()
{
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut().then(function() {
    console.log('User signed out.');
  });
  delete_cookie('RuleEngine')
  delete_cookie('user_role')
  delete_cookie('created_time')
  delete_cookie('account_details')
  delete_cookie('email')
  delete_cookie('name')
}

function notify(position, message, type = 'blackgloss')
{
  $('.' + position).notify(
  {
    message: {
      text: message
    },
    type: 'blackgloss'
  }).show();
}

function update_rule_set()
{
  var message_editor = ace.edit("rule_set_area");
  var event_payload_id = $('#event_payload_id').val();
  var event_payload_state_bool = $('#event_payload_state').is(':checked');
  var event_payload_state = event_payload_state_bool ? 1 : 0;
  var ruleset = message_editor.getValue();
  var retVal = confirm("Do you want to update ruleset ?");
  if (retVal == true)
  {
    $.ajax({
      'url': '/api/v1/ruleset/' + event_payload_id,
      'type': 'PUT',
      'data': {
        'account_id': get_account_id(),
        'ruleset': ruleset,
        'state' : event_payload_state
      },
      beforeSend: function(xhr) {
        xhr.setRequestHeader('Authorization', get_jwt_token());
      },
      success: function(response) {
        if(response['message']){
          notify('top-right', response['message']);
        }else{
          notify('top-right', 'Rulset updated successfully');
        }

      },
      error: function(error) {
        if (error.responseJSON['message']){
          notify('top-right', 'Rulset update failed \n message : ' + error.responseJSON['message'], 'danger');
        }
        else{
          notify('top-right', 'Rulset update failed', 'danger');
        }
      }
    })
  }
  else
  {
    return false;
  }

}

function create_ruleset()
{
  var module_name = $('#module_name').val();
  var payload_type = $('#payload_type').val();
  var major_version = $('#major_version').val();
  var minor_version = $('#minor_version').val();

  var new_rule_set_editor = ace.edit("new_rule_set_editor")
  var ruleset = new_rule_set_editor.getValue()

  $.ajax({
    'url': '/api/v1/ruleset',
    'type': 'POST',
    'data': {
      'module_name': module_name,
      'payload_type': payload_type,
      'major_version': major_version,
      'minor_version': minor_version,
      'ruleset': ruleset,
      'state' : '0',
      'account_id': get_account_id()
    },
    beforeSend: function(xhr) {
      xhr.setRequestHeader('Authorization', get_jwt_token());
    },
    success: function(response) {
      notify('top-right', 'Rulset created successfully');
      setTimeout(document.location.reload(), 2000);
    },
    error: function(error_message) {
      if (error_message.responseJSON['message'])
      {
        notify('top-right', 'Rulset creation failed \n message : ' + error_message.responseJSON['message'], 'danger');

      }
      else
        notify('top-right', 'Rulset creation failed', 'danger');
    }
  })
}

function transform()
{
  //var event_payload_id = $('#event_payload_id').val();
  var central_message_editor = ace.edit("central_message_editor");
  var output_message_editor = ace.edit("output_message");
  var central_message = central_message_editor.getValue();

  $.ajax({
    'url': '/api/v1/transform',
    'type': 'POST',
    "headers": {
      "Content-Type": "application/json",
    },
    data: JSON.stringify({
          //'event_payload_id': event_payload_id,
          'message': central_message,
          'account_id': get_account_id()
    }),
    beforeSend: function(xhr) {
      xhr.setRequestHeader('Authorization', get_jwt_token());
    },
    success: function(response) {
      output_message_editor.setValue(
        JSON.stringify(response['output'], null, '\t'), 1);
    },
    error: function(error) {
      output_message_editor.setValue(
        JSON.stringify(error.responseJSON, null, '\t'), 1);
    }

  })

  output_message_editor.setValue(central_message);
}


function create_rule()
{
  var rule_name = $('#rule_name').val();
  var rule_version = $('#rule_version').val();
  var new_target_schema_editor = ace.edit("new_target_schema_editor");
  var new_rules_editor = ace.edit("new_rules_editor");

  target_schema = new_target_schema_editor.getValue();
  rules = new_rules_editor.getValue();

  $.ajax({
    'url': '/api/v1/rule',
    'method': 'POST',
    beforeSend: function(xhr) {
      xhr.setRequestHeader('Authorization', get_jwt_token());
    },
    data: {
          'rule_name': rule_name,
          'rule_version': rule_version,
          'target_schema': target_schema,
          'rules': rules,
          'account_id': get_account_id()
    },
    success: function(response) {
      notify('top-right', 'Rule created successfully');
      setTimeout(document.location.reload(), 2000);
    },
    error: function(error) {
      if (error.responseJSON['message'])
      {
        notify('top-right', 'Rule creation failed \n message : ' + error.responseJSON['message'], 'danger');

      }
      else
        notify('top-right', 'Rule creation failed', 'danger');
    }
  })
}

function update_rule()
{

  var rule_id = $('#rule_id').val();

  var target_schema_editor = ace.edit("target_schema");
  var rules_editor = ace.edit("rules_editor");

  target_schema = target_schema_editor.getValue();
  rules = rules_editor.getValue();

  var retVal = confirm("Do you want to update rule ?");
  if (retVal == true)
  {

    $.ajax({
      'url': '/api/v1/rule/' + rule_id,
      'type': 'PUT',
      beforeSend: function(xhr) {
        xhr.setRequestHeader('Authorization', get_jwt_token());
      },
      data: {
            'target_schema': target_schema,
            'rules': rules,
            'account_id': get_account_id()
      },
      success: function(response) {
        if(response['message']){
          notify('top-right', response['message']);
        }else{
          notify('top-right', 'Rule Updated successfully');
        }
      },
      error: function(error) {
        if (error.responseJSON['message'])
        {
          notify('top-right', 'Rule update failed \n message : ' + error.responseJSON['message'], 'danger');
        }
        else
          notify('top-right', 'Rule update failed', 'danger');
      }
    })
  }
  else
    return false;


}

function validate_service()
{
  var input_dict = {};
  input_dict['service_name'] = $('#service_name').val();
  var transformation_success_topic = document.getElementsByName('success_topic[]');
  input_dict['transformation_retry_count'] = $('#retry_count').val();
  input_dict['reports_config'] = $('#reports_config').val();
  input_dict['api_push_retry_count'] = $('#api_push_retry_count').val();
  var payload_type = document.getElementsByName('payload_type[]');
  input_dict['webhook_url'] = $('#webhook_url').val();

  input_dict['success_topic'] = [];
  input_dict['payload_type'] = [];

  for (var i = 0; i < transformation_success_topic.length; i++)
  {
    input_dict['success_topic'].push(transformation_success_topic[i].value)
    input_dict['payload_type'].push(payload_type[i].value)
  }
  input_dict['payload_type'][0] = 'default'
  return [true, input_dict]
}

function create_service()
{
  var [validation, input_dict] = validate_service()
  if (!validation)
    notify('top-right', 'Fill all fields');
  else
  {
    $.ajax({
      'url': '/api/v1/service',
      'method': 'POST',
      beforeSend: function(xhr) {
        xhr.setRequestHeader('Authorization', get_jwt_token());
      },
      data: {
          'service_name': input_dict['service_name'],
          'retry_count': input_dict['transformation_retry_count'],
          'success_topic': input_dict['success_topic'],
          'reports_config': input_dict['reports_config'],
          'api_push_retry_count': input_dict['api_push_retry_count'],
          'payload_type': input_dict['payload_type'],
          'account_id': get_account_id(),
          'webhook_url': input_dict['webhook_url']
      },
      success: function(response) {
        notify('top-right', 'Service created successfully');
        setTimeout(document.location = '/services', 2000);
      },
      error: function(error) {
        if (error.responseJSON['message'])
        {
          notify('top-right', 'Service creation failed \n message : ' + error.responseJSON['message'], 'danger');

        }
        else
          notify('top-right', 'Service creation failed', 'danger');
      }
    })
  }
}



function update_service()
{
  var service_id = $("#service_id").val();
  var retVal = confirm("Do you want to update service ?");
  if (retVal == true)
  {
    var [validation, input_dict] = validate_service();
    if (!validation)
      notify('top-right', 'Fill all fields');
    else
    {
      $.ajax({
        'url': '/api/v1/service/' + service_id,
        'type': 'PUT',
        beforeSend: function(xhr) {
          xhr.setRequestHeader('Authorization', get_jwt_token());
          // xhr.setRequestHeader('account_id',get_account_id());
        },
        data: {
              'service_name': input_dict['service_name'],
              'retry_count': input_dict['transformation_retry_count'],
              'success_topic': input_dict['success_topic'],
              'reports_config': input_dict['reports_config'],
              'api_push_retry_count': input_dict['api_push_retry_count'],
              'payload_type': input_dict['payload_type'],
              'account_id': get_account_id(),
              'webhook_url': input_dict['webhook_url']
        },
        success: function(response) {
          notify('top-right', 'Service Updated successfully');
          setTimeout(document.location.reload(), 2000);
        },
        error: function(error) {
          if (error.responseJSON['message']) {
            notify('top-right', 'Service update failed \n message : ' + error.responseJSON['message'], 'danger');
          } else
            notify('top-right', 'Service update failed', 'danger');
        }
      })
    }
  }
  else
    return false;
}

{
  var field = 1;

  function Add_Field()
  {
    field++;
    var objTo = document.getElementById('add_field');
    var divtest = document.createElement("div");
    divtest.setAttribute("class", "form-group removeclass" + field);
    var rdiv = 'removeclass' + field;
    divtest.innerHTML = '<br><input class="form-control" id="payload_type" name="payload_type[]" type="text" placeholder="payload_type" />&nbsp &nbsp<input class="form-control"  id="success_topic" name="success_topic[]" type="text" placeholder="Success Topic" /><span class="input-group-btn"><button class="btn btn-danger"  onclick="Remove_Field(' + field + ')" type="button"><b class="icon-minus">-</b></button></span>';
    objTo.appendChild(divtest);
  }


  function Remove_Field(field)
  {
    $('.removeclass' + field).remove();
    field--;
  }

  function Clear()
  {
    while (field > 1)
    {
      Remove_Field(field);
      field--;
    }
    field = 1;
    $("#service_name").val("");
    $("#retry_count").val("");
    $('#reports_config').val("");
    $('#api_push_retry_count').val("");
    $('#success_topic').val("");
    $('#payload_type').val("");
    $('#webhook_url').val("");
    $("#serviceModalLabel").html("Create New Service")
    $("#service_modal_button").attr("onclick", "create_service()");
    $("#service_modal_button").text("save");
    $("#service_Modal").modal();

  }
}

  function clear_udf()
  {
    var udf_editor = ace.edit("udf_editor",{
                    mode: "ace/mode/python",
                    selectionStyle: "text"});
    udf_editor.setValue("");
    $("#udfModalLabel").html("Create New UDF")
    $("#model_udf_button").attr("onclick", "create_udf()");
    $("#model_udf_button").text("Create");
    $("#udf_model").modal();
  }

// To add more than one new users
// {
//   var user_field=1
//   function add_new_user(){
//     user_field++
//     var objTo = document.getElementById('add_user')
//     var divtest = document.createElement("div");
//     divtest.setAttribute("class", "form-group user_removeclass"+user_field);
//     var rdiv = 'user_removeclass'+user_field;
//     divtest.innerHTML = '</br><input style="width:90px" type="checkbox" name="role[]" value="2"/>&nbsp \
//     <input style="width:20%" class="form-control"  name="new_users_name[]" type="text" placeholder="user_name" id="new_user_name"/>&nbsp \
//     <input style="width:20%" class="form-control" name="new_users_email[]" type="text" placeholder="abc@freshworks.com" id="new_user_email"/> &nbsp \
//       <span class="input-group-btn">\
//       <button class="btn btn-danger btn-add btn-default" type="button" onclick="Remove_User_Field('+ user_field + ')"> \
//               <b class="icon-plus">- \
//         </button> \
//       </span>'
//     objTo.appendChild(divtest)
//     console.log(divtest)
//   }
//
//
// function Remove_User_Field(user_field)
// {
//   console.log("user_remove"+user_field)
//   $('.user_removeclass'+user_field).remove();
//   user_field--
//
// }
//
// }

function export_rules()
{
  $.ajax({
    'url': '/api/v1/export',
    'type': 'POST',
    'data': {
      "account_id": get_account_id()
    },
    beforeSend: function(xhr) {
      xhr.setRequestHeader('Authorization', get_jwt_token());
    },
    success: function(response) {
      var date = new Date();
      var timestamp = date.getTime();
      var file_name = `${get_account_name()}_${timestamp}.json`;
      var retVal = confirm("Do you want to download rules ?");
      if (retVal == true) {
        var dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(response));
        var downloadAnchorNode = document.createElement('a');
        downloadAnchorNode.setAttribute("href", dataStr);

        downloadAnchorNode.setAttribute("download", file_name);
        notify('top-right', 'Successfully exported');
        document.body.appendChild(downloadAnchorNode); // required for firefox
        downloadAnchorNode.click();
        downloadAnchorNode.remove();
      }

    },
    error: function(error) {
      if (error.responseJSON['message'])
      {
        notify('top-right', 'Export failed \n message: ' + error.responseJSON['message', 'danger']);
      }
      else
      {
        notify('top-right', 'Export failed', 'danger');
      }
    }

  })
}


function single_message(){
    // $("#message_editor").hide()
    var topic_name = $("#topic_name").val().trim()
    var partition = $("#partition").val()
    var offset = $("#offset").val()
    console.log(topic_name)
    console.log(partition)
    console.log(offset)
    if(topic_name=='' || partition=='' || offset==''){
      notify('top-right',"Enter all topic, partition and offset values")
    }
    else{
      $("#load").show()
      $.ajax({
        'url': '/api/v1/failed_message',
        'type': 'GET',
        beforeSend: function(xhr) {
          xhr.setRequestHeader('Authorization',get_jwt_token());
          // xhr.setRequestHeader('account_id',get_account_id());
        },
        'data': {
          'topic_name': topic_name,
          'partition': partition,
          'offset': offset
        },
        success: function(response) {
          $("#load").hide()
          // $("#message_editor").show()
            var editor = ace.edit("central_message_editor");
            editor.setValue(JSON.stringify(response["data"],undefined,2))
        },
        error: function(error) {
          $("#load").hide()
          if(error.status == 502)
          {
            notify('top-right', 'Got invalid response! That topic may not exist');
          }
          else if(error.responseJSON['message']) {
            notify('top-right','Invalid Offset or Partition \n message: ' + error.responseJSON['message']);
          }
          else {
            notify('top-right','Connection failed','danger')
          }
        }
    })
  }
}

// function create_account() {
//   var account_name = $("#new_account_name").val()
//   var user_name = $("#user_name").val()
//   var user_email = $("#user_email").val()
//   var user_role = $("input[name='user_role']:checked").val()
//   console.log(user_role)
//   $.ajax({
//     'url':'/api/v1/create_new_account',
//     'type': 'POST',
//     'data': {
//       'account_name': account_name,
//       'user_name': user_name,
//       'user_email': user_email,
//       'user_role': user_role,
//     },
//     beforeSend: function(xhr) {
//       xhr.setRequestHeader('Authorization',get_jwt_token());
//     },
//     success: function(response) {
//       notify('top-right',"successfully create new account");
//       setTimeout(document.location.reload(), 2000);
//
//     },
//     error: function(error) {
//       if(error.responseJSON['message']) {
//         notify('top-right', error.responseJSON['message']);
//       }
//
//     }
//   })
// }

function add_new_user()
{

  $.ajax({
    'url':'/api/v1/user',
    'type': 'POST',
    'dataType': 'json',
    'data': {
      'account_id': get_account_id(),
      'account_name': get_account_name(),
      'name': $("#user_name").val(),
      'email': $('#user_email').val(),
      'role' : $("#dropdown_user_role").val()
    },
    beforeSend: function(xhr) {
      xhr.setRequestHeader('Authorization', get_jwt_token());
    },
    success: function(response) {
      notify('top-right', "successfully add new user");
      setTimeout(document.location.reload(), 2000);

    },
    error: function(error) {
      if (error.responseJSON['message']) {
        notify('top-right', error.responseJSON['message']);
      }

    }
  })
}

function retry_failed_message() {
    var central_message_editor = ace.edit("central_message_editor");
    var central_message = central_message_editor.getValue()
    publish_failed_message(central_message)
}


function retry_permanent_failed_message()
{
  var message_editor = ace.edit("message_editor");
  var message = message_editor.getValue();
  publish_failed_message(message);
}

function publish_failed_message(message)
{
  $.ajax({
    url: '/api/v1/failed_message_producer',
    type: 'POST',
    dataType: 'json',
    data: {
      'message': message,
    },
    beforeSend: function(xhr) {
      xhr.setRequestHeader('Authorization', get_jwt_token());
    },
    success: function(response) {
      notify('top-right', "successfully pushed to failed topic");

    },
    error: function(error) {
      if (error.responseJSON['message'])
      {
        notify('top-right', error.responseJSON['message']);
      }
    }
  })
}

function create_udf() {
  var udf_editor = ace.edit("udf_editor",{
                      mode: "ace/mode/python",
                      selectionStyle: "text"})
  var definition = udf_editor.getValue()

  $.ajax({
    'url': '/api/v1/udf',
    'type': 'POST',
    'data': {
      'definition': definition,
      'account_id': get_account_id()
    },
    beforeSend: function(xhr) {
      xhr.setRequestHeader('Authorization', get_jwt_token());
    },
    success: function(response) {
      notify('top-right', 'your method is successfully saved');
      setTimeout(document.location.reload(), 2000);
    },
    error: function(error_message) {
      if (error_message.responseJSON['message']) {
        notify('top-right', 'Method creation failed \n message : ' +
              error_message.responseJSON['message'], 'danger');

      } else
        notify('top-right', 'Method creation failed', 'danger');
    }
  })

}

function update_udf_definition() {
    var udf_editor = ace.edit("udf_editor",{
                        mode: "ace/mode/python",
                        selectionStyle: "text"})
    var definition = udf_editor.getValue()
    var retVal = confirm("Do you want to update method ?");
    if (retVal == true) {
      $.ajax({
        'url': '/api/v1/udf',
        'type': 'PUT',
        'data': {
          'definition': definition,
          'account_id': get_account_id()
        },
        beforeSend: function(xhr) {
          xhr.setRequestHeader('Authorization', get_jwt_token());
        },
        success: function(response) {
          if(response['message']){
            notify('top-right', response['message']);
          }else{
            notify('top-right', 'Method is updated successfully');
          }
          setTimeout(document.location.reload(), 2000);

        },
        error: function(error_message) {
          if (error_message.responseJSON['message']) {
            notify('top-right', 'Method update failed \n message : ' +
            error_message.responseJSON['message'], 'danger');

          } else
            notify('top-right', 'Method update failed', 'danger');
          setTimeout(document.location.reload(), 2000);
        }
      })
  }

}

function update_udf_state(id,name,status)
{
  console.log(status)
  var retVal = confirm("Do you want to update this method ?");
  if (retVal==true) {
    $.ajax ({
      "url": '/api/v1/udf/'+id,
      "type": "PUT",
      "data": {
        "id": id,
        "account_id": get_account_id(),
        "name": name,
        "status":status
      },
      "beforeSend": function(request) {
        request.setRequestHeader("Authorization", api_key);
      },
      success: function(data,testStatus,xhr) {
        if(xhr.status == 304)
          notify('top-right',"Accepted/Rejected methods can not be updated")
        else
          notify('top-right', "Successfully Updated")
        setTimeout(document.location.reload(), 20000);

      },
      failed: function(error) {
        console.log(error.responseJSON['message'])
        if (error.responseJSON['message']){
           notify('top-right', error.responseJSON['message'])
         }
         else {
           notify('top-right',"something went wrong")
         }
         setTimeout(document.location.reload(), 20000);
      }
    });
  }
}

var history_data_table = undefined;
var history_table_data = []
var audit_log_response = []
function showHistory(target_type, target_id, page = 0, page_size = 4) {
  if(history_data_table != undefined) {
    history_data_table.destroy();
  }

  history_table_data = []
  audit_log_response = []

  payload =  {
    'account_id' : get_account_id(),
    'page' : page,
    'page_size' : page_size
  }

  if(target_type == 'rules'){
    payload['rule_id'] = target_id
  }else if(target_type == 'rulesets'){
    payload['ruleset_id'] = target_id
  }else if(target_type == 'udfs'){
    payload['udf_id'] = target_id
  }

  $.ajax({
      "url": 'api/v1/revisions/' + target_type,
      "type": "GET",
      "async" : false,
      'headers':{
        'Authorization' : get_jwt_token()
      },
      data: payload,
      success: function(response){
        audit_log_response = response.data;
      },
      error: function(error){
        alert("Audit logs api failed")
      }
  });
  audit_log_response.forEach(function (item) {
    var obj = {}

    obj["version_no"] = item.version_no
    obj["username"] =  item.username
    obj["created_at"] = item.created_at
    obj["diff"] = `<a style='text-align:center;cursor:pointer;' onclick=showAuditDiff(${item.id},'diff','${target_type}')>View</a>`
    obj['version'] = `<a style='text-align:center;cursor:pointer;' onclick=showAuditDiff(${item.id},'version','${target_type}')>View</a>`

    promotion_info = item.promotion_info;
    if(promotion_info === null){
      obj['promotion'] = 'unpromoted'
    }else{
      promotion_info = JSON.parse(promotion_info);
      message = ""
      promoted_pods = Object.keys(promotion_info);
      promoted_pods.forEach(function (pod){
        if(promotion_info[pod]['status'] == 'success'){
          message = `${message} Promoted to <b>${pod}</b> by
                    ${promotion_info[pod]['promoted_by']} at
                    ${promotion_info[pod]['time']} <br>`
        }else if(promotion_info[pod]['status'] == 'failed'){
          message = `${message} Promotion failed in <b>${pod}</b> by
                    ${promotion_info[pod]['promoted_by']} at
                    ${promotion_info[pod]['time']} <br>`
        }
      });

      obj['promotion'] = message;

    }

    history_table_data.push(obj)

  });

  history_data_table = $("#history_table").DataTable({
    dom: '<"dom_element">frtip',
    "pageLength": page_size,
    data: history_table_data,
    "columns": [{'data': 'version_no'}, {'data': 'username'},{'data': 'promotion'},{'data': 'created_at'}, {'data' : 'diff'}, {'data' : 'version'}],
    pagingType: "simple",
    language: {
      paginate: {
        previous: "<",
        next: ">"
      }
    },
    searching: false,
    info: false,
    order: [[ 0, "desc" ]],
    fnDrawCallback: function (param) {
      // hiding and showing previous, next buttons
      //console.log($(this).find('tbody tr').length)
      $('#history_table_paginate').show();
      if($(this).find('tbody tr').length < page_size && page == 0){
          $('#history_table_paginate').hide();
      } else{
        if(page >= 0){
          $('#history_table_previous').removeClass('disabled');
          }
        if ($(this).find('tbody tr').length >= page_size){
            $('#history_table_next').removeClass('disabled');
        }
      }
      // adding next button click logic
      $('.paginate_button.next:not(.disabled)', this.api().table().container())
      .on('click', function(){
          page++;
          showHistory(target_type, target_id, page);
      });
      // adding previous button click logic
      $('.paginate_button.previous:not(.disabled)', this.api().table().container())
      .on('click', function(){
        page--;
        if(page < 0) { page = 0;}
          showHistory(target_type, target_id, page);
       });
    }
  });

  $('#history').modal(true);
}

function showDiffJSON(old_json, new_json, id){

  let span = null;
  const diff = JsDiff.diffLines(old_json, new_json),
      display = document.getElementById(id),
      fragment = document.createDocumentFragment();

  diff.forEach((part) => {
    const color = part.added ? 'green' :
      part.removed ? 'red' : 'black';
    span = document.createElement('span');
    span.style.color = color;
    span.appendChild(document
      .createTextNode(part.value));
    fragment.appendChild(span);
  });

  display.innerHTML=""
  display.appendChild(fragment);
}

function showAuditDiff(id, type, target_type){

  object = filterJsonObject(audit_log_response, 'id', id)
  if(target_type == 'rules'){
    old_json = object.previous_rules;
    new_json = object.rules;
  }else if(target_type == 'rulesets'){
    old_json = object.previous_ruleset;
    new_json = object.ruleset;
  }else if(target_type == 'udfs'){
    old_json = object.previous_definition;
    new_json = object.definition;
  }

  if(type == 'diff'){
    showDiffJSON(old_json, new_json, 'version_content');
  }else{
    version_div = document.getElementById('version_content');

    version_div.innerHTML = ""
    version_div.innerHTML = new_json
  }

}

var promote_data_table = undefined
var local_api_response = []
var remote_api_response = []

function fetchPromotePods(id){
  $.ajax({
        'url': `api/v1/remote_mappings_for_account?account_id=${get_account_id()}`,
        'type': 'GET',
        'headers':{
          'Authorization' : get_jwt_token()
        },
        success: function(response){
            var pods_dropdown = document.getElementById(id);
            response.data.forEach(function (item){
                var option = document.createElement("option");
                option.text = item.pod;
                option.value = item.remote_account_id;
                pods_dropdown.add(option);
            });
        },
        error: function(error){
          alert("Error in getting remote accounts mapping")
        }
      })
}

function fetchPromoteData(){
  var promote_type = $("#promote_type").val();
  var selectedPod = $("#promote_pod option:selected").html();
  var promote_pod = selectedPod;
  var promote_account_id = $("#promote_pod").val()
  if((promote_type != 'select' && selectedPod == 'Select') || (promote_type == 'select' && selectedPod != 'Select')){
    generatePromoteTable({"data": []}, [], 'rules')
  }
  else if (promote_type != 'select' && selectedPod != 'Select'){
    $.ajax({
        'url': `/api/v1/remote?account_id=${get_account_id()}&entity=${promote_type}&pod=${promote_pod}`,
        'type': 'GET',
        'async' : false,
        'headers':{
          'Authorization' : get_jwt_token()
        },
        success: function(remote_response){
          remote_api_response = remote_response

          $.ajax({
            'url': `/api/v1/unpromoted?account_id=${get_account_id()}&entity=${promote_type}&pod=${promote_pod}`,
            'type': 'GET',
            'async' : false,
            'headers':{
              'Authorization' : get_jwt_token()
            },
            success: function(unpromoted_changes){
              $('.promote_button').css("display", "block");
              generatePromoteTable(unpromoted_changes, remote_api_response, promote_type)

            },
            error: function(local_error){
              showErrorAlert(local_error)
            }
        });

        },
        error: function(remote_error){
          showErrorAlert(remote_error)
        }
    });

  }else{
    alert('Please choose all fields ')
  }

}

function showErrorAlert(error){
  console.log(error);
  var errorMsg = 'Sorry.. Something wrong happened.. See console for more info'
  if (error.hasOwnProperty('responseJSON')) {
    errorMsg = error.responseJSON
  }
  if (error.hasOwnProperty('responseJSON') && error.responseJSON.hasOwnProperty('message')) {
    errorMsg = error.responseJSON['message']
  }
  alert(errorMsg);
}

function filterJsonObject(data, key, value) {
  for (var i = 0; i < data.length; i++) {
    var object = data[i];
    if(object[key] == value){
      return object
    }
  }
  return "{}"
}

function filterJson(data, key, value, required) {
  for (var i = 0; i < data.length; i++) {
    var object = data[i];
    if(object[key] == value){
      return object[required]
    }
  }
  return "{}"
}

function filterRule(data, rule) {
  for (var i = 0; i < data.length; i++) {
    var object = data[i];
    if(object['name'] == rule['name'] && object['version'] == rule['version']){
      return object;
    }
  }
  return undefined;
}

function filterRuleSet(data, ruleset) {
  for (var i = 0; i < data.length; i++) {
    var object = data[i];
    if(object['payload_type'] == ruleset['payload_type'] && object['major_version'] == ruleset['major_version'] && object['minor_version'] == ruleset['minor_version']){
      return object;
    }
  }
  return undefined;
}

function filterUDF(data, udf) {
  for (var i = 0; i < data.length; i++) {
    var object = data[i];
    if(object['name'] == udf['name']){
      return object;
    }
  }
  return undefined;
}

var promotion_data = [];

function generatePromoteTable(local_response, remote_response, promote_entity_type){
  var promote_data = [];
  promotion_data = [];

  local_response.data.forEach(function (item) {

  if(promote_entity_type == 'rules'){
    local_json = item.rules;
  }else if(promote_entity_type == 'rulesets'){
    local_json = item.ruleset;
  }else if(promote_entity_type == 'udfs'){
    local_json = item.definition;
  }

  promotion_data.push(item);

  var obj = {};
  obj['checkbox'] = `<input type="checkbox" id="promote_checkbox_${item.id}" value="${item.id}">`;
  if(promote_entity_type == 'rules'){
    obj['name'] = item.name + "_" + item.version;
  }else if(promote_entity_type == 'rulesets'){
    obj['name'] = item.payload_type + "_" + item.major_version + "." + item.minor_version;
  }else if(promote_entity_type == 'udfs'){
    obj['name'] = item.name;
  }
  obj['version'] = `${item.version_no}`
  obj['diff'] = `<button onclick=showPromoteDiff(${item.id},'${promote_entity_type}')>View ${promote_entity_type}</button>`;
  obj['status'] = `<div id="status${item.id}"><span class="badge badge-secondary">Yet to promote</span></div>`;

  promote_data.push(obj);

  });

  if(promote_data_table != undefined) {
    promote_data_table.destroy();
  }

  promote_data_table = $('#promote_content_table').DataTable({
      data: promote_data,
      "columns": [{'data': 'checkbox'}, {'data': 'name'},{'data': 'version'},{'data': 'diff'}, {'data' : 'status'}],
      aoColumnDefs: [
      {
        bSortable: false,
        aTargets: [ 0 ]
      }]
    });

}

function showPromoteDiff(id, entity){
  $('#promote_diff').modal(true);

  local_title = document.getElementById('local_title_title');
  diff_title = document.getElementById('promote_diff_final_title');
  promote_diff = document.getElementById('promote_diff_changes');
  local_data = document.getElementById('promote_local_final');

  diff_title.innerHTML = "Diff"
  object = filterJsonObject(promotion_data, 'id', id)
  if(entity == 'rules'){
    payload = object.rules
    local_title.innerHTML = "Final rule that gets promoted"
  }else if(entity == 'rulesets'){
    payload = object.ruleset
    local_title.innerHTML = "Final ruleset that gets promoted"
  }else if(entity == 'udfs'){
    payload = object.definition
    local_title.innerHTML = "Final udf that gets promoted"
  }else{
    payload = {}
  }

  last_promoted = object.last_promoted

  local_data.innerHTML = "";
  local_data.innerHTML = payload

  showDiffJSON(last_promoted, payload, 'promote_diff_changes')

}

function mergeTwoJSON(json1, json2){
  if(objectType(JSON.parse(json1)) == 'Array' && objectType(JSON.parse(json2)) == 'Array'){
    mergeJson = $.extend([], JSON.parse(json1), JSON.parse(json2));
  }else{
    mergeJson = $.extend({}, JSON.parse(json1), JSON.parse(json2));
  }
  return mergeJson;
}

function objectType(object) {
    var stringConstructor = "test".constructor;
    var arrayConstructor = [].constructor;
    var objectConstructor = ({}).constructor;

    if (object === null) {
        return "null";
    }
    else if (object === undefined) {
        return "undefined";
    }
    else if (object.constructor === stringConstructor) {
        return "String";
    }
    else if (object.constructor === arrayConstructor) {
        return "Array";
    }
    else if (object.constructor === objectConstructor) {
        return "Object";
    }
    {
        return "";
    }
}


function selectAllCheckboxes(val) {
  $('input[id^=promote_checkbox_]').each(function (el) {
    $(this).prop('checked', val.checked)
  })
}

function updateStatus(id, status, success, error){
  if(status){
    var successMsg = "";
    if(success.hasOwnProperty('message')){
      successMsg = success['message']
    }
    $(`#status${id}`).html(`<span class="badge badge-success">Success</span><br><p style="color: green">${successMsg}</p>`);
    $(`#promote_checkbox_${id}`).prop("checked", false);
    $(`#promote_checkbox_${id}`).remove();
  }else{
    console.log(error);
    var errorMsg = 'Sorry.. Something wrong happened.. See console for more info'
    if (error.hasOwnProperty('responseJSON')) {
      errorMsg = error.responseJSON
    }
    if (error.hasOwnProperty('responseJSON') && error.responseJSON.hasOwnProperty('message')) {
      errorMsg = error.responseJSON['message']
    }
    $(`#status${id}`).html(`<span class="badge badge-danger">Failed</span><br><p style="color: red">${errorMsg}</p>`);
  }
}

function constructPayloadAndCallAPI(entity, pod, item){
  local_account_id = get_account_id();
  data = {}
  data['account_id'] = local_account_id;
  data['pod'] = pod
  data['entity'] = entity
  data['version_no'] = item.version_no
  if(entity == 'rules'){
    data['entity_id'] = item.rule_id;
    local_rule = item.rules
    remote_rule = filterRule(remote_api_response.data, item);
    if(remote_rule == undefined){
      data['remote_entity_id'] = 0;
    }else{
      data['remote_entity_id'] = remote_rule['id'];
    }

  }else if(entity == 'rulesets'){
    data['entity_id'] = item.ruleset_id;
    local_ruleset = item.ruleset
    remote_ruleset = filterRuleSet(remote_api_response.data, item);
    if(remote_ruleset == undefined){
      data['remote_entity_id'] = 0;
    }else{
      data['remote_entity_id'] = remote_ruleset['event_payload_id'];
    }

  }else if(entity == 'udfs'){
    data['entity_id'] = item.udf_id;
    data['remote_entity_id'] = 0;
  }

  callPromoteAPI(data, function(response){
    updateStatus(item.id, true, response, {});
  },function(error){
    console.log(error)
    updateStatus(item.id, false, {}, error);
  });
}

function callPromoteAPI(data, callback, error_callback){
  $.ajax({
    url: 'api/v1/promote',
    type: 'POST',
    async: false,
    data: data,
    headers: {
      'Authorization' : get_jwt_token()
    },
    success: function(response) {
      if (callback && typeof (callback) === 'function') {
        callback.call(this, response)
      }
    },
    error: function(error) {
      if (error_callback && typeof (error_callback) === 'function') {
        error_callback.call(this, error)
      }
    }
  });
}

function promote(){
  var promoteIds = []

  $("input[id^='promote_checkbox_']").each(function (el) {
    if (this.checked) {
      promoteIds.push(parseInt(this.value))
    }
  })

  if(promoteIds.length < 1 ){
    alert('Please select atlest one row');
  }else{
      if(confirm("Are you sure you want to promote these?")){

        promote_entity_type = $("#promote_type").val();
        pod = $("#promote_pod option:selected").html();
        promotion_data.forEach(function (item){
          id = item.id
          if(promoteIds.includes(id)){
            constructPayloadAndCallAPI(promote_entity_type, pod, item);
          }
        });
    }
  }
}

var compare_local_api_response = []
var compare_remote_api_response = []
function fetchComparisonData(){

  compare_local_api_response = []
  compare_remote_api_response =[]

  var comparison_entity = $("#comparison_entity").val();
  var compareSelectedPod = $("#comparison_pod option:selected").html();
  var comparison_pod = compareSelectedPod;
  var compare_account_id = $("#comparison_pod").val()
  if((comparison_entity != 'select' && compareSelectedPod == 'Select') || (comparison_entity == 'select' && compareSelectedPod != 'Select')){
    generateComparisonTable([], [], 'rules')
  }
  else if (comparison_entity != 'select' && compareSelectedPod != 'Select'){

    $.ajax({
        'url': `/api/v1/remote?account_id=${get_account_id()}&entity=${comparison_entity}&pod=${comparison_pod}`,
        'type': 'GET',
        'async' : false,
        'headers':{
          'Authorization' : get_jwt_token()
        },
        success: function(remote_response){
          compare_remote_api_response = remote_response.data;

          $.ajax({
            'url': `/api/v1/${comparison_entity}?account_id=${get_account_id()}`,
            'type': 'GET',
            'async' : false,
            'headers':{
              'Authorization' : get_jwt_token()
            },
            success: function(local_response){
             compare_local_api_response = local_response.data;

            },
            error: function(local_error){
              showErrorAlert(local_error)
            }
          });

          $('.comparison_button').css("display", "block");
          generateComparisonTable(compare_local_api_response, compare_remote_api_response, comparison_entity);


        },
        error: function(remote_error){
          showErrorAlert(remote_error)
        }
    });
  }else{
    alert('Please choose all fields ')
  }
}

var compare_data_table = undefined;
var compare_data = []
function generateComparisonTable(local_response, remote_response, comparison_entity){

  compare_data = []

  counter = 0;
  local_response.forEach(function (item) {

    name = ""
    remote_id = 0
    if(comparison_entity == 'rules'){
      local_json = item.rules;
      name = item.name + "_" + item.version
      remote_data = filterRule(remote_response, item);
      if(remote_data !=undefined){
        remote_json = remote_data['rules']
        remote_id = remote_data['id']
      }else{
        remote_json = "{}";
      }

    }else if(comparison_entity == 'rulesets'){
      local_json = item.ruleset;
      name = item.payload_type + "_" + item.major_version + "." + item.minor_version;
      remote_data = filterRuleSet(remote_response, item)
      if(remote_data !=undefined){
        remote_json = remote_data['ruleset']
        remote_id = remote_data['id']
      }else{
        remote_json = "[]";
      }
    }else if(comparison_entity == 'udfs'){
      local_json = item.definition
      name = item.name;
      remote_data = filterUDF(remote_response, item)
      if(remote_data != undefined){
        remote_json = remote_data['definition']
        remote_id = remote_data['id']
      }else{
        remote_json = "";
      }
    }

    if(!isLocalRemoteSame(local_json, remote_json, comparison_entity)){

      var obj = {}

      var obj = {};
      obj['s_no'] = counter + 1;
      obj['name'] = name;
      obj['diff'] = `<button onclick=showCompareDiff(${item.id},${remote_id},'${comparison_entity}')>View ${comparison_entity} diff</button>`;

      compare_data.push(obj)
      counter = counter + 1;
    }


  });


  if(compare_data_table != undefined) {
    compare_data_table.destroy();
  }

  compare_data_table = $('#comparison_content_table').DataTable({
      data: compare_data,
      "columns": [{'data': 's_no'}, {'data': 'name'},{'data': 'diff'}],
      aoColumnDefs: [
      {
        bSortable: false,
        aTargets: [ 0 ]
      }]
    });

}

function isLocalRemoteSame(local_json, remote_json, entity){
  if(entity == 'rules' || entity == 'rulesets'){
    return _.isEqual(JSON.parse(local_json),JSON.parse(remote_json))
  }else if(entity == 'udfs'){
    return _.isEqual(local_json, remote_json)
  }
}


function showCompareDiff(local_id, remote_id, entity){

   $('#compare_diff').modal(true);

  local_title = document.getElementById('compare_local_title');
  remote_title = document.getElementById('compare_remote_title');
  diff_title = document.getElementById('compare_diff_title');

  local_payload = document.getElementById('compare_local_payload');
  remote_payload = document.getElementById('compare_remote_payload');
  diff_payload = document.getElementById('compare_diff_payload');


  local_title.innerHTML = window.location.hostname;
  remote_title.innerHTML = $("#comparison_pod option:selected").html();

  local_object = filterJsonObject(compare_local_api_response, 'id', local_id);
  remote_object = filterJsonObject(compare_remote_api_response, 'id', remote_id);

  if(entity == 'rules'){
    local_json = local_object.rules

  }else if(entity == 'rulesets'){
    local_json = local_object.ruleset

  }else if(entity == 'udfs'){
    local_json = local_object.definition
  }else{
    local_json = ""
  }

  if(remote_object == "{}"){
    remote_json = "{}"
    if(entity == 'udfs'){
      remote_json = ""
    }
  }else{
    if(entity == 'rules'){
      remote_json = remote_object.rules
    }else if(entity == 'rulesets'){
      remote_json = remote_object.ruleset

    }else if(entity == 'udfs'){
      remote_json = remote_object.definition
    }else{
      remote_json = ""
    }
  }


  local_payload.innerHTML = "";
  local_payload.innerHTML = local_json

  remote_payload.innerHTML = "";
  remote_payload.innerHTML = remote_json

  showDiffJSON(remote_json, local_json, 'compare_diff_payload')

}

function showLoading(obj) {
  $(obj).loader('show');
}

// This function is used to hide loading
function hideLoading (obj) {
  $(obj).loader('hide');
}


function checkRoleAndRemoveButton(id, role){
  if(role == 0){
    $(id).css("display", "none");
  }
}

function add_new_topic()
{

  topic_name = $('#configure_topic_name').val()
  partitions = $('#topic_partitions').val()
  rpm = $('#topic_rpm').val()
  topic_modules = $('#topic_modules').val();

  if(topic_name.length > 0 && partitions.length > 0 && rpm.length > 0 && topic_modules.length > 0){
    $.ajax({
      'url':'/api/v1/topics',
      'type': 'POST',
      'data': {
        'account_id': get_account_id(),
        'topic_name': topic_name,
        'partitions': partitions,
        'rpm': rpm,
        'modules': topic_modules
      },
      beforeSend: function(xhr) {
        xhr.setRequestHeader('Authorization', get_jwt_token());
      },
      success: function(response) {
        notify('top-right', response['message']);
      },
      error: function(error) {
        if (error.responseJSON['message']) {
          notify('top-right', error.responseJSON['message']);
        }
      }
    })
  }else{
    alert('Please fill all fields')
  }
}
