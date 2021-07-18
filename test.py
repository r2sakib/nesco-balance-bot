page = """ <!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <!-- Meta, title, CSS, favicons, etc. -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	  
    <title>NESCO Prepaid Consumer Portal</title>
	<link rel="shortcut icon" href="logo.png" />
	

    <!-- Bootstrap -->
    <link href="../vendors/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link href="../vendors/font-awesome/css/font-awesome.min.css" rel="stylesheet">
    <!-- NProgress -->
    <link href="../vendors/nprogress/nprogress.css" rel="stylesheet">
    <!-- iCheck -->
    <link href="../vendors/iCheck/skins/flat/green.css" rel="stylesheet">
    <!-- bootstrap-wysiwyg -->
    <link href="../vendors/google-code-prettify/bin/prettify.min.css" rel="stylesheet">
    <!-- Select2 -->
    <link href="../vendors/select2/dist/css/select2.min.css" rel="stylesheet">
    <!-- Switchery -->
    <link href="../vendors/switchery/dist/switchery.min.css" rel="stylesheet">
    <!-- starrr -->
    <link href="../vendors/starrr/dist/starrr.css" rel="stylesheet">
    <!-- bootstrap-daterangepicker -->
    <link href="../vendors/bootstrap-daterangepicker/daterangepicker.css" rel="stylesheet">

    <!-- Custom Theme Style -->
    <link href="../build/css/custom.min.css" rel="stylesheet">
  </head>

<style>


table.table1 {}
table.table1 tr:nth-child(even) {
	background-color: #DADED4;
}
table.table1 td, th {
	text-align: center;
  border: 0px solid #2F4F4F;
}

table.table2 {border: none;}
table.table2 tr {border: none;}
table.table2 td {border: none;}


.split {
  height: 100%;
  width: 50%;
  position: fixed;
  z-index: 1;
  top: 0;
  overflow-x: hidden;
  padding-top: 20px;
}

.left {
  left: ;
}

.right {
  right: 0;
}


@media screen and (min-width: 480px) {
        .modal-dialog {
          max-width: 480px; 
        }
    }
	
@media screen {
  #printSection {
      display: none;
  }
}

@media print {
	
  body * {
    visibility:hidden;
	page-break-after: avoid;
    page-break-before: avoid;
  }
  #printSection, #printSection * {
    visibility:visible;
  }
  #printSection {
    position:absolute;
    left:0;
    top:0;
  }
}

@page { 
	size: auto;  
	margin-left: 8mm; 
	margin-right: 8mm; 
	margin-top: 8mm; 
	margin-bottom: 8mm; 
}


</style>


        
        
	<body style="background-color:#9DC88D;">   <!-- class="nav-md" -->
		<div class="container body">
      <div class="main_container">
        <!-- page content color sample: :#A3BCB6  -->
        <div class="right_col" role="main" style="background-color:#9DC88D;">
		
          <div class="">
            <div class="page-title">
			<marquee onmouseover="this.stop();" onmouseout="this.start();" direction="left">
              <h2 style="color:red">
            </div>
			</marquee>
            <div class="clearfix"></div>
			
			
			
			<div class="col-md-offset-1 col-sm-offset-1 col-md-10 col-sm-10 col-xs-12">
				<div class="panel panel-primary" style="border-color:#266150;">
					<div class="panel-heading" style="background-color:#266150; text-align: center;">
						<a href='http://182.160.102.19:89/' style='color:white;' ><i class="fa fa-home fa-2x pull-left"></i></a>
						<span style='font-size: 16px;'>Enter your Customer Number or Meter Number</span>
				
					</div>
					<div class="panel-body">
						<form id="customer-form" method="post"  data-parsley-validate class="form-horizontal form-label-middle" action="/index.php">
							<div class="form-group">
								<label class="control-label col-md-3 col-sm-3 col-xs-12" for="cust_no" style="color:black;">Customer Number or Meter Number <span class="required" style="color:red;">*</span>
								</label>
								<div class="col-md-6 col-sm-6 col-xs-12">
									<input type="text" id="cust_no" name="cust_no" value="71050717" class="form-control col-md-6 col-sm-6 col-xs-12">
									</input>
									<label class="col-md-12 col-sm-12 col-xs-12" style="color:red;"></label>
							
								</div>
							</div>
							<div class="form-group">
								<div class="col-md-12 col-sm-12 col-xs-12 col-md-offset-3 col-sm-offset-3">
								
								 	<button class="btn btn-primary" type="submit" name="rech_hist" style="color:white; background-color:#266150; margin-bottom:7px; width: 175px;">Show Recharge History</button>
									<button class="btn btn-primary" type="submit" name="usage_hist" style="color:white; background-color:#266150; margin-bottom:7px; width: 175px;">Consumption History</button>
									<button class="btn btn-primary" type="submit" name="reset" style="color:white; background-color:#266150; margin-bottom:7px;">Reset</button>								
								</div>
							</div>

						</form>
					</div>
				</div>
			</div>
		
			 <div class="col-md-offset-1 col-sm-offset-1 col-md-10 col-sm-10 col-xs-12" style="margin-top:25px;">
				<div class="panel panel-primary" style="border-color:#266150;">
					<div class="panel-body">
					
						<form class="form-horizontal form-label-left">

						  <div class="form-group">
							<label class="control-label col-md-2 col-sm-2 col-xs-12" style="color:black;">Customer Name</label>
							<div class="col-md-10 col-sm-10 col-xs-12">
								<input type="text" class="form-control" disabled="disabled" value="MOST. ZESMIN ARA KHATUN">
							</div>
							
						  </div>
						  <div class="form-group">
							<label class="control-label col-md-2 col-sm-2 col-xs-12" style="color:black;">Customer Address</label>
							<div class="col-md-10 col-sm-10 col-xs-12">
							  <input type="text" class="form-control" disabled="disabled" value="M.M. ROAD  ,SIRAJGONJ">
							</div>
						  </div>
						  <div class="form-group">
							<label class="control-label col-md-2 col-sm-2 col-xs-12" style="color:black;">Mobile</label>
							<div class="col-md-4 col-sm-4 col-xs-12">
							  <input type="text" class="form-control" disabled="disabled" value="01772099153">
							</div>
							<label class="control-label col-md-2 col-sm-2 col-xs-12" style="color:black;">S&D Name</label>
							<div class="col-md-4 col-sm-4 col-xs-12">
							  <input type="text" class="form-control" disabled="disabled" value="Sirajganj  S&D1 ">
							</div>
						  </div>
						  <div class="form-group">
							<label class="control-label col-md-2 col-sm-2 col-xs-12" style="color:black;">Customer Number</label>
							<div class="col-md-2 col-sm-2 col-xs-12">
							  <input type="text" class="form-control" disabled="disabled" value="71050717">
							</div>
							<label class="control-label col-md-2 col-sm-2 col-xs-12" style="color:black;">Meter Number</label>
							<div class="col-md-2 col-sm-2 col-xs-12">
							  <input type="text" class="form-control" disabled="disabled" value="12011011169">
							</div>
							<label class="control-label col-md-2 col-sm-2 col-xs-12" style="color:black;">Sanction Load (KW)</label>
							<div class="col-md-2 col-sm-2 col-xs-12">
							  <input type="text" class="form-control" disabled="disabled" value="2">
							</div>
						  </div>
						  
						  <div class="form-group">
							<label class="control-label col-md-2 col-sm-2 col-xs-12" style="color:black;">Sanction Tariff</label>
							<div class="col-md-3 col-sm-3 col-xs-12">
							  <input type="text" class="form-control" disabled="disabled" value="LT-A">
							</div>
							
							<label class="control-label col-md-4 col-sm-4 col-xs-12" style="color:black;">Remaining balance (Tk.)<small style="color:red;"></br>(Time: 18 July 2021 12:00:00 AM)</small></label>
							<div class="col-md-3 col-sm-3 col-xs-12">
							  <input style="color:red; font-weight: bold;" type="text" class="form-control" disabled="disabled" value="-74.59">
							</div>
							
							
						  </div>
						  
						  
						</form>
							
						</br>
						
						  <div class="x_title">
							<h2 style="color:black;">Recharge History</h2>
							
							<div class="clearfix"></div>
						  </div>
						<table id="datatable" class="table table-striped table-bordered table1 col-md-12 col-sm-12 col-xs-12">
						
                      <thead>
                        <tr style="color:white; background-color:#4D774E;">
                          <th>Order Number</th>
                          <th>Token Number</th>
                          <th>Meter Rent (Tk.)</th>
                          <th>Demand Charge (Tk.)</th>
						  <th>PFC (Tk.)</th>
                          <th>VAT (Tk.)</th>
						  <th>Debt Amount (Tk.)</th>
						  <th>Rebate (Tk.)</th>
						  <th>Energy Amount (Tk.)</th>
                          <th>Recharge Amount (Tk.)</th>
						  <th>Estimated Purchase Unit</th>
						  <th>Payment Media</th>
                          <th>Recharge Date</th>
						  <th>Remote Recharge</th>
                        </tr>
                      </thead>
								
                      <tbody><tr style="color:black;"><td style="color:blue; font-weight: bold; "><a onclick="setEventId(0)" data-toggle="modal" data-target="#myModal" href="javascript:void(0)">572989352351899648</a></td><td>1728-4060-3414-6222-9760</td><td>40</td><td>60</td><td>0</td><td>47.62</td><td>0</td><td>-9.03</td><td>861.41</td><td>1000</td><td>174.5</td><td>NAGAD</td><td>08/07/2021 11:41:57</td><td>Success</td></tr><tr style="color:black;"><td style="color:blue; font-weight: bold; "><a onclick="setEventId(1)" data-toggle="modal" data-target="#myModal" href="javascript:void(0)">568751114040909824</a></td><td>3077-0060-0153-7159-5972</td><td>40</td><td>60</td><td>0</td><td>42.86</td><td>0</td><td>-8.09</td><td>765.23</td><td>900</td><td>157.69</td><td>NAGAD</td><td>26/06/2021 19:00:42</td><td>Failed</td></tr><tr style="color:black;"><td style="color:blue; font-weight: bold; "><a onclick="setEventId(2)" data-toggle="modal" data-target="#myModal" href="javascript:void(0)">558848053466112000</a></td><td>3235-9114-3079-9460-8996</td><td>0</td><td>0</td><td>0</td><td>90.48</td><td>0</td><td>-17.92</td><td>1827.44</td><td>1900</td><td>334.73</td><td>NAGAD</td><td>30/05/2021 11:09:29</td><td>Success</td></tr><tr style="color:black;"><td style="color:blue; font-weight: bold; "><a onclick="setEventId(3)" data-toggle="modal" data-target="#myModal" href="javascript:void(0)">550930329389768704</a></td><td>3569-7205-6424-9387-9299</td><td>40</td><td>60</td><td>0</td><td>90.48</td><td>0</td><td>-17.52</td><td>1727.04</td><td>1900</td><td>318.89</td><td>NAGAD</td><td>08/05/2021 14:47:16</td><td>Success</td></tr><tr style="color:black;"><td style="color:blue; font-weight: bold; "><a onclick="setEventId(4)" data-toggle="modal" data-target="#myModal" href="javascript:void(0)">546894323653025792</a></td><td>5382-9098-1250-2878-2610</td><td>0</td><td>0</td><td>0</td><td>47.62</td><td>0</td><td>-9.43</td><td>961.81</td><td>1000</td><td>192.06</td><td>ROCKET</td><td>27/04/2021 11:29:37</td><td>Success</td></tr><tr style="color:black;"><td style="color:blue; font-weight: bold; "><a onclick="setEventId(5)" data-toggle="modal" data-target="#myModal" href="javascript:void(0)">543271033269571584</a></td><td>1520-7761-3193-9435-4991</td><td>40</td><td>60</td><td>0</td><td>47.62</td><td>0</td><td>-9.03</td><td>861.41</td><td>1000</td><td>174.5</td><td>NAGAD</td><td>17/04/2021 11:31:58</td><td>Success</td></tr><tr style="color:black;"><td style="color:blue; font-weight: bold; "><a onclick="setEventId(6)" data-toggle="modal" data-target="#myModal" href="javascript:void(0)">536854007118483456</a></td><td>4492-9519-4023-4021-9182</td><td>0</td><td>0</td><td>0</td><td>47.62</td><td>0</td><td>-9.43</td><td>961.81</td><td>1000</td><td>192.06</td><td>NAGAD</td><td>30/03/2021 18:32:59</td><td>Success</td></tr><tr style="color:black;"><td style="color:blue; font-weight: bold; "><a onclick="setEventId(7)" data-toggle="modal" data-target="#myModal" href="javascript:void(0)">533256356015820800</a></td><td>4365-5857-4147-8118-8425</td><td>0</td><td>0</td><td>0</td><td>28.57</td><td>0</td><td>-5.66</td><td>577.09</td><td>600</td><td>124.8</td><td>ROCKET</td><td>20/03/2021 20:17:12</td><td>Success</td></tr><tr style="color:black;"><td style="color:blue; font-weight: bold; "><a onclick="setEventId(8)" data-toggle="modal" data-target="#myModal" href="javascript:void(0)">529854812771766272</a></td><td>1226-5956-3173-6447-8824</td><td>40</td><td>60</td><td>0</td><td>23.81</td><td>0</td><td>-4.32</td><td>380.51</td><td>500</td><td>90.43</td><td>Sirajganj S&D-1 UVS1</td><td>11/03/2021 11:00:41</td><td>Unsend</td></tr>	
                      </tbody>
                    </table>
										
					</div>
				</div>
			</div>
			

            
            </div>
          </div>
        </div>
		
		<!-- Modal -->
		<!-- Modal -->
<div class = "modal fade" id = "myModal" tabindex = "-1" role = "dialog" 
   aria-labelledby = "myModalLabel" aria-hidden = "true">
   
   <div class = "modal-dialog">
      <div class = "modal-content">
         

         <div class = "modal-header" >
            <button type = "button" class = "close" data-dismiss = "modal" aria-hidden = "true">
                  &times;
            </button>
            
            <h4 class = "modal-title" id = "myModalLabel">
              Order Information
            </h4>  
         </div>
		 <div id="printThis" style="width: 480px;">
         
         <div class = "modal-body">
					

					<h1 style="text-align:center; color:black; ">Northern Electricity Supply Company Ltd.</h1>
					<table class="table2" style="width:100%">
					  <tr>
						<td style="text-align:left;"><label style="color:black; font-size: 18px;">Date: </label></td>
						<td style="text-align:right;"><label style="color:black; font-size: 18px;"><span id="purchaseDate"></span></label></td>
					  </tr>
					  <tr>
						<td style="text-align:left;"><label style="color:black; font-size: 18px;">Order No.: </label></td>
						<td style="text-align:right;"><label style="color:black; font-size: 18px; "><span id="orderNo"></span></label></td>
					  </tr>
					  <tr>
						<td style="text-align:left;"><label style="color:black; font-size: 18px;">Meter No.: </label></td>
						<td style="text-align:right;"><label style="color:black; font-size: 18px;">12011011169</label></td>
					  </tr>
					  <tr>
						<td style="text-align:left;"><label style="color:black; font-size: 18px;">Customer No.: </label></td>
						<td style="text-align:right;"><label style="color:black; font-size: 18px;">71050717</label></td>
					  </tr>
					  <tr>
						<td style="text-align:left;"><label style="color:black; font-size: 18px;">Customer Name: </label></td>
						<td style="text-align:right;"><label style="color:black; font-size: 18px;">MOST. ZESMIN ARA KHATUN</label></td>
					  </tr>
					  <tr>
						<td style="text-align:left;"><label style="color:black; font-size: 18px;">Tariff Program: </label></td>
						<td style="text-align:right;"><label style="color:black; font-size: 18px;">LT-A</label></td>
					  </tr>
					  <tr>
						<td style="text-align:left;"><label style="color:black; font-size: 18px;">Sanction Load: </label></td>
						<td style="text-align:right;"><label style="color:black; font-size: 18px;">2</label></td>
					  </tr>
					  <tr>
						<td style="text-align:left;"><label style="color:black; font-size: 18px;">S&D/ESU: </label></td>
						<td style="text-align:right;"><label style="color:black; font-size: 18px;">Sirajganj  S&D1 </label></td>
					  </tr>
					  <tr>
						<td style="text-align:left;"><label style="color:black; font-size: 18px;">Vending Station: </label></td>
						<td style="text-align:right;"><label style="color:black; font-size: 18px;"><span id="saleName"></span></label></td>
					  </tr>
					  
					</table>

					<hr />
					<table class="table2" style="width:100%">
						<tr>
							<td style="text-align:left;"><label style="color:black; font-size: 18px;">Energy Cost: </label></td>
							<td style="text-align:right;"><label style="color:black; font-size: 18px;"><span id="purchaseAmount"></span> Tk</label></td>
						</tr>
						<tr>
							<td style="text-align:left;"><label style="color:black; font-size: 18px;">Rebate (1%): </label></td>
							<td style="text-align:right;"><label style="color:black; font-size: 18px;"><span id="subsidyAmount"></span> Tk</label></td>
						</tr>
						<tr>
							<td style="text-align:left;"><label style="color:black; font-size: 18px;">Paid debt: </label></td>
							<td style="text-align:right;"><label style="color:black; font-size: 18px;"><span id="debtAmount"></span> Tk</label></td>
						</tr>
						<tr>
							<td style="text-align:left;"><label style="color:black; font-size: 18px;">Demand Charge: </label></td>
							<td style="text-align:right;"><label style="color:black; font-size: 18px;"><span id="demandCharge"></span> Tk</label></td>
						</tr>
						<tr>
							<td style="text-align:left;"><label style="color:black; font-size: 18px;">Meter Rent: </label></td>
							<td style="text-align:right;"><label style="color:black; font-size: 18px;"><span id="rent"></span> Tk</label></td>
						</tr>
						<tr>
							<td style="text-align:left;"><label style="color:black; font-size: 18px;">VAT (5%): </label></td>
							<td style="text-align:right;"><label style="color:black; font-size: 18px;"><span id="tax"></span> Tk</label></td>
						</tr>
						<tr>
							<td style="text-align:left;"><label style="color:black; font-size: 18px;">PFC: </label></td>
							<td style="text-align:right;"><label style="color:black; font-size: 18px;"><span id="pfc"></span> Tk</label></td>
						</tr>
						<tr>
							<td style="text-align:left;"><label style="color:black; font-size: 18px;">Total Amount: </label></td>
							<td style="text-align:right;"><label style="color:black; font-size: 18px;"><span id="totalAmount"></span> Tk</label></td>
							
						</tr>
						<tr>
							<td style="text-align:left;"><label style="color:black; font-size: 18px;">Paid Amount: </label></td>
							<td style="text-align:right;"><label style="color:black; font-size: 18px;"><span id="paidAmount"></span> Tk</label></td>
						</tr>
						
						
					</table>
					
					<hr />
					<table class="table2" style="width:100%">
						<tr>
							<td style="text-align:center;"><label style="color:red; font-size: 30px;"><span id="token"></span></label></td>
							
						</tr>
						<tr>
							<td style="text-align:left;"><label style="color:black; ">Please press Enter after each 20 digits Token, then continue to another new token.</label></td>
							
						</tr>
						<tr>
							<td style="text-align:left;"><label style="color:black; ">Estimate of units (KWh):</label>
								<label style="color:black;"><span id="purchaseEnergy"></span></label></td>
							
						</tr>
						<tr>
							<td></br></br></td>
						</tr>
						<tr>
							<td style="color:black; text-align:center;"><label>This token is generated from prepaid.nesco.gov.bd.</label></td>
						</tr>
						
					</table>
					
					
					
					<br />
					
					
	
			
			
         </div>
		 </div>
         
         <div class = "modal-footer">
			<button id="btnPrint" type="button" class="btn btn-primary">Print</button>
            <button type = "button" class = "btn btn-default" data-dismiss = "modal">
               Close
            </button>
         </div>
         
      </div><!-- /.modal-content -->
   </div><!-- /.modal-dialog -->
  
</div><!-- /.modal -->

        <!-- /page content -->
		

		</div>
    </div>
	
	

	

    <!-- jQuery -->
    <script src="../vendors/jquery/dist/jquery.min.js"></script>
    <!-- Bootstrap -->
    <script src="../vendors/bootstrap/dist/js/bootstrap.min.js"></script>
    <!-- FastClick -->
    <script src="../vendors/fastclick/lib/fastclick.js"></script>
    <!-- NProgress -->
    <script src="../vendors/nprogress/nprogress.js"></script>
    <!-- bootstrap-progressbar -->
    <script src="../vendors/bootstrap-progressbar/bootstrap-progressbar.min.js"></script>
    <!-- iCheck -->
    <script src="../vendors/iCheck/icheck.min.js"></script>
    <!-- bootstrap-daterangepicker -->
    <script src="../vendors/moment/min/moment.min.js"></script>
    <script src="../vendors/bootstrap-daterangepicker/daterangepicker.js"></script>
    <!-- bootstrap-wysiwyg -->
    <script src="../vendors/bootstrap-wysiwyg/js/bootstrap-wysiwyg.min.js"></script>
    <script src="../vendors/jquery.hotkeys/jquery.hotkeys.js"></script>
    <script src="../vendors/google-code-prettify/src/prettify.js"></script>
    <!-- jQuery Tags Input -->
    <script src="../vendors/jquery.tagsinput/src/jquery.tagsinput.js"></script>
    <!-- Switchery -->
    <script src="../vendors/switchery/dist/switchery.min.js"></script>
    <!-- Select2 -->
    <script src="../vendors/select2/dist/js/select2.full.min.js"></script>
    <!-- Parsley -->
    <script src="../vendors/parsleyjs/dist/parsley.min.js"></script>
    <!-- Autosize -->
    <script src="../vendors/autosize/dist/autosize.min.js"></script>
    <!-- jQuery autocomplete -->
    <script src="../vendors/devbridge-autocomplete/dist/jquery.autocomplete.min.js"></script>
    <!-- starrr -->
    <script src="../vendors/starrr/dist/starrr.js"></script>
    <!-- Custom Theme Scripts -->
    <script src="../build/js/custom.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>


	<script>	
		function setEventId(row_id){
			var tempArray = jQuery.parseJSON('[{"customerNo":"71050717","customerName":"MOST. ZESMIN ARA KHATUN","meterNo":"12011011169","orderNo":"572989352351899648","saleName":"NAGAD","purchaseEnergy":"174.5","debtAmount":"0","tax":"47.62","mcostAmount":"100","subsidyAmount":"-9.03","purchaseAmount":"861.41","penaltyAmount":"0","totalAmount":"1000","newCurrencyError":"0","principleAmount":"952.38","fee":null,"purchaseDate":"08\/07\/2021 11:41:57","token":"1728-4060-3414-6222-9760","rent":"40","demandCharge":"60","pfc":"0","remoteRechargeStatus":"Success"},{"customerNo":"71050717","customerName":"MOST. ZESMIN ARA KHATUN","meterNo":"12011011169","orderNo":"568751114040909824","saleName":"NAGAD","purchaseEnergy":"157.69","debtAmount":"0","tax":"42.86","mcostAmount":"100","subsidyAmount":"-8.09","purchaseAmount":"765.23","penaltyAmount":"0","totalAmount":"900","newCurrencyError":"0","principleAmount":"857.14","fee":null,"purchaseDate":"26\/06\/2021 19:00:42","token":"3077-0060-0153-7159-5972","rent":"40","demandCharge":"60","pfc":"0","remoteRechargeStatus":"Failed"},{"customerNo":"71050717","customerName":"MOST. ZESMIN ARA KHATUN","meterNo":"12011011169","orderNo":"558848053466112000","saleName":"NAGAD","purchaseEnergy":"334.73","debtAmount":"0","tax":"90.48","mcostAmount":"0","subsidyAmount":"-17.92","purchaseAmount":"1827.44","penaltyAmount":"0","totalAmount":"1900","newCurrencyError":"0","principleAmount":"1809.52","fee":null,"purchaseDate":"30\/05\/2021 11:09:29","token":"3235-9114-3079-9460-8996","rent":"0","demandCharge":"0","pfc":"0","remoteRechargeStatus":"Success"},{"customerNo":"71050717","customerName":"MOST. ZESMIN ARA KHATUN","meterNo":"12011011169","orderNo":"550930329389768704","saleName":"NAGAD","purchaseEnergy":"318.89","debtAmount":"0","tax":"90.48","mcostAmount":"100","subsidyAmount":"-17.52","purchaseAmount":"1727.04","penaltyAmount":"0","totalAmount":"1900","newCurrencyError":"0","principleAmount":"1809.52","fee":null,"purchaseDate":"08\/05\/2021 14:47:16","token":"3569-7205-6424-9387-9299","rent":"40","demandCharge":"60","pfc":"0","remoteRechargeStatus":"Success"},{"customerNo":"71050717","customerName":"MOST. ZESMIN ARA KHATUN","meterNo":"12011011169","orderNo":"546894323653025792","saleName":"ROCKET","purchaseEnergy":"192.06","debtAmount":"0","tax":"47.62","mcostAmount":"0","subsidyAmount":"-9.43","purchaseAmount":"961.81","penaltyAmount":"0","totalAmount":"1000","newCurrencyError":"0","principleAmount":"952.38","fee":null,"purchaseDate":"27\/04\/2021 11:29:37","token":"5382-9098-1250-2878-2610","rent":"0","demandCharge":"0","pfc":"0","remoteRechargeStatus":"Success"},{"customerNo":"71050717","customerName":"MOST. ZESMIN ARA KHATUN","meterNo":"12011011169","orderNo":"543271033269571584","saleName":"NAGAD","purchaseEnergy":"174.5","debtAmount":"0","tax":"47.62","mcostAmount":"100","subsidyAmount":"-9.03","purchaseAmount":"861.41","penaltyAmount":"0","totalAmount":"1000","newCurrencyError":"0","principleAmount":"952.38","fee":null,"purchaseDate":"17\/04\/2021 11:31:58","token":"1520-7761-3193-9435-4991","rent":"40","demandCharge":"60","pfc":"0","remoteRechargeStatus":"Success"},{"customerNo":"71050717","customerName":"MOST. ZESMIN ARA KHATUN","meterNo":"12011011169","orderNo":"536854007118483456","saleName":"NAGAD","purchaseEnergy":"192.06","debtAmount":"0","tax":"47.62","mcostAmount":"0","subsidyAmount":"-9.43","purchaseAmount":"961.81","penaltyAmount":"0","totalAmount":"1000","newCurrencyError":"0","principleAmount":"952.38","fee":null,"purchaseDate":"30\/03\/2021 18:32:59","token":"4492-9519-4023-4021-9182","rent":"0","demandCharge":"0","pfc":"0","remoteRechargeStatus":"Success"},{"customerNo":"71050717","customerName":"MOST. ZESMIN ARA KHATUN","meterNo":"12011011169","orderNo":"533256356015820800","saleName":"ROCKET","purchaseEnergy":"124.8","debtAmount":"0","tax":"28.57","mcostAmount":"0","subsidyAmount":"-5.66","purchaseAmount":"577.09","penaltyAmount":"0","totalAmount":"600","newCurrencyError":"0","principleAmount":"571.43","fee":null,"purchaseDate":"20\/03\/2021 20:17:12","token":"4365-5857-4147-8118-8425","rent":"0","demandCharge":"0","pfc":"0","remoteRechargeStatus":"Success"},{"customerNo":"71050717","customerName":"MOST. ZESMIN ARA KHATUN","meterNo":"12011011169","orderNo":"529854812771766272","saleName":"Sirajganj S&D-1 UVS1","purchaseEnergy":"90.43","debtAmount":"0","tax":"23.81","mcostAmount":"100","subsidyAmount":"-4.32","purchaseAmount":"380.51","penaltyAmount":"0","totalAmount":"500","newCurrencyError":"0","principleAmount":"476.19","fee":null,"purchaseDate":"11\/03\/2021 11:00:41","token":"1226-5956-3173-6447-8824","rent":"40","demandCharge":"60","pfc":"0","remoteRechargeStatus":"Unsend"}]');
			document.querySelector("#orderNo").innerHTML = tempArray[row_id].orderNo;
			document.querySelector("#token").innerHTML = tempArray[row_id].token;
			document.querySelector("#rent").innerHTML = tempArray[row_id].rent;
			document.querySelector("#demandCharge").innerHTML = tempArray[row_id].demandCharge;
			document.querySelector("#tax").innerHTML = tempArray[row_id].tax;
			document.querySelector("#pfc").innerHTML = tempArray[row_id].pfc;
			document.querySelector("#subsidyAmount").innerHTML = tempArray[row_id].subsidyAmount;
			document.querySelector("#purchaseAmount").innerHTML = tempArray[row_id].purchaseAmount;
			document.querySelector("#totalAmount").innerHTML = tempArray[row_id].totalAmount;
			document.querySelector("#purchaseEnergy").innerHTML = tempArray[row_id].purchaseEnergy;
			document.querySelector("#saleName").innerHTML = tempArray[row_id].saleName;
			document.querySelector("#purchaseDate").innerHTML = tempArray[row_id].purchaseDate;
			document.querySelector("#debtAmount").innerHTML = tempArray[row_id].debtAmount;
			document.querySelector("#paidAmount").innerHTML = tempArray[row_id].totalAmount;

		}
		
		//for printing
		document.getElementById("btnPrint").onclick = function () {
			printElement(document.getElementById("printThis"));
			document.title = "Recharge Token";
			window.print();
		}

		function printElement(elem) {
			var domClone = elem.cloneNode(true);
			
			var $printSection = document.getElementById("printSection");
			
			if (!$printSection) {
				var $printSection = document.createElement("div");
				$printSection.id = "printSection";
				document.body.appendChild($printSection);
			}
			
			$printSection.innerHTML = "";
			
			$printSection.appendChild(domClone);
		}
		
	</script>
	
	
	
  </body>
</html> """

from bs4 import BeautifulSoup

soup = BeautifulSoup(page, 'lxml')

def last_recharge():
	table_rows = soup.findAll('tr')

	data = []
	for table_cell in table_rows[1]:
		data.append(table_cell.text)

	return {'date': data[-2],
			'energy ammount': data[8],
			'recharge ammount': data[9],
			'unit': data[10], 
			'method': data[11],
			'remote': data[12]}

print(data)