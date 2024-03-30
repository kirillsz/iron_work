<?php
	require_once 'access.php';

if (isset($_POST) && !empty($_POST['telephone'])){
	$ip = '1.2.3.4';
	$domain = 'k701.ru';
	$pipeline_id = 5396578;
	$user_amo = 6299323;
	
	$phone = $_POST['telephone'];
	$action_data = $_POST['actionType'];
	
	

$data3 = 
[
	[
	"name"=> "Заявка с сайта $domain",
	"custom_fields_values" => 
		
	   [
					[
						"field_id" => 1242967, 
						"values" => 
						[
							[ 
								"value" => $action_data
							]
						   
						]
					],
					[
						"field_id" => 1242975,
						"values" => [
							[
								"value" => $domain]]
						]
		],
	"_embedded"=>
	[
		"metadata" => 
	   [
				"category" => "forms",
				"form_id" => 1,
				"form_name" => "Форма на сайте",
				"form_page" => $domain,
				"form_sent_at" => strtotime(date("Y-m-d H:i:s")),
				"ip" => $ip,
				"referer" => $domain
			],
	   "contacts"=>
	   [
		  [
			 "first_name"=>"Автоконтакт $phone",
			 "created_at"=>strtotime(date("Y-m-d H:i:s")),
			 "responsible_user_id"=> $user_amo,
			 "custom_fields_values"=> [
					[
				   "field_code"=>"PHONE",
				   "values"=>
				   [
					  [
						 "enum_code"=>"WORK",
						 "value"=> $phone     # Указанный контактом телефон
					  ]
				   ]
				],
					[
						"field_id" => 771589, # Принятие пользовательского соглашения
						"values" => 
						[
							[ 
								"value" => true 
							]
						   
						]
					],
			  ],
			 
		  ]
	   ],
	   
	   
	],
	"created_at"=>strtotime(date("Y-m-d H:i:s")),
	"responsible_user_id"=>$user_amo,
	"pipeline_id"=>$pipeline_id,
 ]
];


$method = "/api/v4/leads/complex";

$headers = [
	'Content-Type: application/json',
	'Authorization: Bearer ' . $access_token,
];

$curl = curl_init();
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_USERAGENT, 'amoCRM-API-client/1.0');
curl_setopt($curl, CURLOPT_URL, "https://$subdomain.amocrm.ru".$method);
curl_setopt($curl, CURLOPT_CUSTOMREQUEST, 'POST');
curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($data3));
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
curl_setopt($curl, CURLOPT_HEADER, false);
curl_setopt($curl, CURLOPT_COOKIEFILE, 'amo/cookie.txt');
curl_setopt($curl, CURLOPT_COOKIEJAR, 'amo/cookie.txt');
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, 0);
$out = curl_exec($curl);

}
	echo "У вас нет прав для этого действия";



