package com.example.espaolquechua;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.ToggleButton;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;


public class MainActivity extends AppCompatActivity {

    EditText inputTxt;
    Button btnTraducir;
    TextView TxtTraducido;
    Boolean bandera;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputTxt = findViewById(R.id.inputTxt);
        btnTraducir = findViewById(R.id.btnTraducir);
        TxtTraducido = findViewById(R.id.TxtTraducido);
        bandera=true;

        btnTraducir.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (inputTxt.getText().toString().isEmpty()){
                    Toast.makeText(MainActivity.this, "Ingrese un texto", Toast.LENGTH_LONG).show();
                    return;
                }
                if (bandera){
                    traducirQuEs(inputTxt.getText().toString());
                }else {
                    traducirEsQu(inputTxt.getText().toString());
                }
            }
        });

        final ToggleButton toggleButton=(ToggleButton)findViewById(R.id.toggleButton1);

        toggleButton.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                // TODO Auto-generated method stub

                if(isChecked){
                    //
                    bandera = !bandera;
                    toggleButton.setBackgroundResource(R.drawable.derecha);
                }else{
                    //
                    bandera = !bandera;
                    toggleButton.setBackgroundResource(R.drawable.izquierda);
                }
            }
        });
    }
    private void traducirEsQu(final String txt){
        String url = "https://secret-depths-37808.herokuapp.com/es-qu?txt=" + txt;

        StringRequest postResquest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                TxtTraducido.setText(response);
                Toast.makeText(MainActivity.this, "Traducido del español", Toast.LENGTH_LONG).show();
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.e("Error", error.getMessage());
            }
        }) {
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("accept", "application/json");

                return params;
            }
        };
        Volley.newRequestQueue(this).add(postResquest);
    }

    private void traducirQuEs(final String txt){
        String url = "https://secret-depths-37808.herokuapp.com/qu-es?txt=" + txt;

        StringRequest postResquest = new StringRequest(Request.Method.POST, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                TxtTraducido.setText(response);
                Toast.makeText(MainActivity.this, "Runasimi manta tikrasqa", Toast.LENGTH_LONG).show();
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.e("Error", error.getMessage());
            }
        }) {
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<>();
                params.put("accept", "application/json");

                return params;
            }
        };
        Volley.newRequestQueue(this).add(postResquest);
    }
}